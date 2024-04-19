---

date: 2024-03-29 00:07:00-0500
categories: blog
author: Andrew van der Stock
author_image: /assets/images/people/staff_andrew.jpg
layout: blogpost
title: OWASP Data Leak Notification
excerpt_separator: <!--more-->

---

In late February 2024, after receiving a few support requests, the OWASP Foundation became aware of a misconfiguration of OWASP’s old Wiki web server, leading to a data leak involving decade+-old member resumes. 

<!--more-->

- **Who is affected?** If you were an OWASP member from 2006 to around 2014 and provided your resume as part of joining OWASP, we advise assuming your resume was part of this leak.
- **What data was exposed?** The resumes contained names, email addresses, phone numbers, physical addresses, and other personally identifiable information. 
- **Why was the data collected?** OWASP collected resumes as part of the early membership process, whereby members were required in the 2006 to 2014 era to show a connection to the OWASP community. OWASP no longer collects resumes as part of the membership process.
- **What steps has OWASP taken to rectify the leak?** We have disabled directory browsing, reviewed the web server and Media Wiki configuration for other security issues, removed the resumes from the wiki site altogether, and purged the CloudFlare cache to prevent further access. Lastly, we have requested that the information be removed from the Web Archive.
- **Who will OWASP notify?** We are bringing this issue to the broader public's attention with abundant caution. As many of the individuals affected by this leak are no longer with OWASP and the age of the data is between ten and 18 years old, a great deal of the personal details included in this leak are significantly out of date, making contact difficult. Regardless, we will contact the email addresses discovered during our investigations.
- **How does OWASP protect current membership data?** We apply modern cloud-based security best practices such as two-factor authentication, minimal access, and resiliency to protect our membership data. We also purposefully collect only minimal information for OWASP membership to minimize any potential data loss in the future.
- **I think I am affected. What do I need to do?** OWASP has already removed your information from the Internet, so no immediate action on your part is required. Nothing needs to be done if the information at risk is outdated. However, if the information is current, such as containing your mobile phone number, please take the usual precautions when answering unsolicited emails, mail, or phone calls.

We recognize the significance of this leak, especially considering the OWASP Foundation’s emphasis on cybersecurity. We apologize to those affected by the leak and are committed to ensuring that this does not happen again. We are reviewing our data retention policies and will be implementing additional security measures to prevent future leakes.

> Revision (19 April 2024): The incident should have been labeled a "leak" rather than a "breach". The information was exposed to the public internet due to a misconfiguration, not because of an attack. We do not know if the exposed information was accessed, or by whom. The press release has been revised to clarify this.
