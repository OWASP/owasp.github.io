# A Comparison Between the Real User ID and the Effective User ID is not Enough to Prevent Privilege Escalation

**_Article originally posted in [Websec's blog](https://websec.ca/publication/Blog/comparison-between-real-user-id-and-effective-user-id-is-not-enough-to-prevent-privilege-escalation)._**

## Introduction

Subtle bugs that result in security vulnerabilities tug at our emotions. They evoke the very reasons many of us were drawn to security in the first place. It's that exhilarating sensation of thinking beyond the ordinary, of delving into those overlooked details that many might miss. The allure lies in understanding and feeling the intricacies, reminding us of the depth and humanity behind every line of code. However, they also serve as humbling reminders of our fallibility — that things can still go awry no matter how careful we are.

In this article, I'll discuss a bug pattern I've detected across multiple projects recently, which isn’t really new. The recent vulnerability advisories and CVEs should be out soon. Given its subtleness, it has stayed hidden, lurking in the shadows for so long. As security professionals, we must shed light on these overlooked bugs. Only through diligent documentation and shared knowledge can we hope to eradicate them.

## The Problem With Only Comparing Real User ID and Effective User ID as a Security Check

In Unix-like operating systems, every process has a real user ID and an effective user ID. The system uses these IDs to determine the process's permissions for accessing resources. In most cases, a process's real user ID and effective user ID are the same, but they can differ in certain situations, such as when the setuid bit is set in executables, as shown in the following:

% cat getuid_example1.c  

```

\#include <stdio.h>  
\#include <unistd.h>  

int main() {
    printf("Real user ID: %d\n", getuid());
    printf("Effective user ID: %d\n", geteuid());
    return 0;
}
```

% gcc getuid_example1.c -o getuid_example1  
% ./getuid_example1  
**Real user ID: 501**  
**Effective user ID: 501**  

% sudo chown root getuid_example1  
% sudo chmod u+s getuid_example1  
% ./getuid_example1  
**Real user ID: 501**  
**Effective user ID: 0**  

Applications that perform critical operations, such as loading dynamic libraries or executing code under the current effective user ID, can use the C functions getuid() and geteuid() to obtain the user ID values and use them as part of security checks within their applications. Comparing the values returned by getuid() and geteuid() is a common technique among developers to detect applications executing with the setuid bit set and to prevent possible privilege escalation bugs. Let’s look at an example of these functions used as a security check.

% cat libfoo.c  

```

\#include <stdio.h>  

void foo() {
    printf("Malicious library loaded.\n");
}
```

%gcc -shared -fPIC libfoo.c -o libfoo.so  
% cat getuid_example2.c  

```

\#include <stdio.h>  
\#include <dlfcn.h>  
\#include <unistd.h>  

int main() {
    printf("Real user ID: %d\n", getuid());
    printf("Effective user ID: %d\n", geteuid());
    if (geteuid() != getuid()) {
        printf("Setuid apps should not pass!\n");
        return 1;
    }
    void *handle = dlopen("<ABSOLUTE PATH TO libfoo.so>", RTLD_LAZY);
    if (!handle) {
        fprintf(stderr, "%s\n", dlerror());
        return 1;
    }
    void (*foo)() = dlsym(handle, "foo");
    if (foo) {
        foo();
    } else {
        fprintf(stderr, "Could not locate the function.\n");
    }
    dlclose(handle);
    return 0;
}
```

% gcc getuid_example2.c -ldl -o getuid_example2  
% ./getuid_example2  
**Real user ID: 501**  
**Effective user ID: 501**  
**Malicious library loaded.**  

% sudo chown root getuid_example2  
% sudo chmod u+s getuid_example2  
% ./getuid_example2  
**Real user ID: 501**  
**Effective user ID: 0**  
**Setuid apps should not pass!**  

## The Oversight

While this security check seems robust, there is a critical situation that developers should be mindful of if they only rely on comparing getuid() and geteuid(). An application can also run with other group’s permissions if the bit setgid comes into play. Let’s rewrite the previous example to see the implications more clearly.

% cat getuid_example3.c  

```

\#include <stdio.h>  
\#include <dlfcn.h>  
\#include <unistd.h>  

int main() {
    if (geteuid() == getuid()) {
        printf("Not running setuid, we can continue safely (or can we?).\n");
        printf("Real user ID: %d\n", getuid());
        printf("Effective user ID: %d\n", geteuid());
        printf("Group ID: %d\n", getgid());
        printf("Effective group ID: %d\n", getegid());
        void *handle = dlopen("<ABSOLUTE PATH TO libfoo.so>", RTLD_LAZY);
        if (!handle) {
            fprintf(stderr, "%s\n", dlerror());
            return 1;
        }
        void (*foo)() = dlsym(handle, "foo");
        if (foo) {
            foo();
        } else {
            fprintf(stderr, "Could not locate the function.\n");
        }
        dlclose(handle);
    }
    return 0;
}
```

% gcc getuid_example3.c -ldl -o getuid_example3  
% ./getuid_example3  
**Not running setuid, we can continue safely (or can we?).**  
**Real user ID: 501**  
**Effective user ID: 501**  
**Group ID: 20**  
**Effective group ID: 20**  
**Malicious library loaded.**  

The real user ID vs. effective user ID is enough to prevent setuid applications, but what about setgid applications? Suppose developers don’t check for this bit. In that case, using the getuid() and geteuid() comparison as a security check will not prevent malicious users from reaching the critical section of the code and obtaining code execution with the group permissions set in that executable.

% sudo chgrp test getuid_example3  
% sudo chmod g+s getuid_example3  
% ./getuid_example3  
**Not running setuid, we can continue safely (or can we?).**  
**Real user ID: 501**  
**Effective user ID: 501**  
**Group ID: 20**  
**Effective group ID: 888**  
**Malicious library loaded.**  

## Abusing This Bug

Let’s look at CVE-2019-19520. Attackers could elevate privileges to the “auth” group in OpenBSD through the utility xlock installed by default. In this case, the application read an unsanitized environment variable path that loaded a driver with dlopen(). Attackers simply needed to point the environment variable to a malicious driver that would get executed:

```
env -i LIBGL_DRIVERS_PATH=. /usr/X11R6/bin/xlock -display :66
```

And this is only one scenario. As with other subtle bugs, the logic of vulnerable applications differs in every application, so the exploitation method and impact will vary.

## The Fix

The correct way of preventing these possible privilege escalation situations is to also check and compare the real group ID and the effective group ID with getgid() and getegid():

```
if (geteuid() == getuid() && getgid() == getegid())
```

And, of course, never trust user input that could be used to load external code.

I wrote a CodeQL query if you want to detect this problem and other variants in your own C/C++ applications. The latest copy and other queries detecting variants of this vulnerability are found in my [CodeQL queries repository](https://github.com/cldrn/codeql-queries). Checkmarx customers can also detect this weakness in their applications by adding the corresponding [Checkmarx rule](https://github.com/cldrn/checkmarx-queries/blob/main/getuid-geteuid-comparison.cx) to your database.

## Conclusions

In conclusion, understanding the difference between real user ID (UID), effective user ID (EUID), real group ID (GID), and effective group ID (EGID) is essential for software developers as it plays a pivotal role in UNIX-like operating systems, ensuring correct access to resources. Recognizing that a mere comparison of getuid() and geteuid() is insufficient to prevent security threats.

While this is a subtle bug, its impact varies depending on the permissions and operations performed by the application. It highlights the importance of employing robust security measures, such as adequately handling permissions, using Linux capabilities, and implementing mandatory access controls. Furthermore, it underscores the need for correct permission configuration and to avoid running programs with elevated privileges unless necessary. We can create more secure applications through vigilance and understanding of these mechanisms.

And, of course, by continuing to share these odd, subtle, and vulnerable code patterns with the community.

# Additional References
- [https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2015-5198](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2015-5198)
- [https://cgit.freedesktop.org/~aplattner/libvdpau/commit/?id=d1f9c16b1a8187110e501c9116d21ffee25c0ba4](https://cgit.freedesktop.org/~aplattner/libvdpau/commit/?id=d1f9c16b1a8187110e501c9116d21ffee25c0ba4)
- [https://www.openwall.com/lists/oss-security/2019/12/04/5](https://www.openwall.com/lists/oss-security/2019/12/04/5)
- [https://github.com/bcoles/local-exploits/blob/master/CVE-2019-19520/openbsd-authroot](https://github.com/bcoles/local-exploits/blob/master/CVE-2019-19520/openbsd-authroot)



