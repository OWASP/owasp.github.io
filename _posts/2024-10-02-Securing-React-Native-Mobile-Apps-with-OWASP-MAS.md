---

date: 2024-10-02 00:00:00-0700
categories: blog
author: Julia Mezher
author_image: /assets/images/people/leader_julia_mezher.png
layout: blogpost
title: Securing React Native Mobile Apps with OWASP MAS
excerpt_separator: <!--more-->

---

React Native is a popular cross-platform mobile development framework that allows developers to build native-looking apps for iOS and Android using a single codebase. Like any other software, React Native apps are also vulnerable to a variety of security threats.

<!--more-->

## 1. Securing each part of the app

To secure a React Native app you should analyse all its parts and how they communicate. This requires an understanding of each block: React Native, iOS, and Android platforms and Bridge between them.

The React Native app uses JavaScript that is run on the JS engine. Understanding native JS engines and Hermes engine from Facebook is also necessary as they have different threat vectors. Using native JS engines makes extracting minified JS code from application bundles easy, while [Hermes had several reported vulnerabilities](https://cve.mitre.org/cgi-bin/cvekey.cgi?keyword=hermes) in the past.

## 2. Assessing React Native apps with OWASP guides

It is also important to follow general mobile application security best practices, such as those described in OWASP guides. While there are no React Native-specific guides, OWASP provides guidance on how to improve the security of native apps, protecting them from common threats and vulnerabilities:

* [OWASP Mobile Application Security Verification Standard](https://mas.owasp.org/MASVS/)
* [OWASP Mobile Application Security Testing Guide](https://mas.owasp.org/MASTG/)
* [OWASP Cheat Sheet Series ](https://cheatsheetseries.owasp.org)

OWASP React Native guides can be used to assess platform-specific security controls, while OWASP JavaScript guides can be used to cover most of the remaining assessment areas:

* [OWASP Application Security Verification Standard](https://owasp.org/www-project-application-security-verification-standard/)
* [OWASP Secure coding guide](https://owasp.org/www-project-secure-coding-practices-quick-reference-guide/stable-en/02-checklist/05-checklist)

The common area for assessment in each cross-platform app is the way methods are bridged between native and non-native parts (like, how JavaScript and native code are communicating). For example, bridged methods may lack obfuscation making platform-specific security controls more visible for reverse engineers. The resilience sections of [OWASP MASTG](https://mas.owasp.org/MASTG/) can serve as a guide to protect against reverse engineering and tampering because they describe concepts that can be applied to cross-platform apps.

## 3. React Native libraries: Secure choice

JavaScript brings to React Native one of its most painful stepping stones: Managing a large number of dependencies and dealing with vulnerabilities in them. Integrating dependency checkers like [OWASP Dependency-Check](https://owasp.org/www-project-dependency-check/) or GitHub Dependabot into the CI/CD process becomes a must-have for React Native apps.

Many React Native libraries are ported from the JavaScript ecosystem, but they may not be suitable for mobile apps, especially for security-sensitive functionality.

A secure React Native library is:

* **Without vulnerabilities:** The library doesn’t have known vulnerabilities and it has a reasonable history of patching known vulnerabilities.
* **Without open security issues:** Review GitHub issues and PRs to see how the maintainers respond to security issues.
* **Actively maintained and supported** by multiple people. The security-related library should be supported by people with security and cryptography expertise, and ideally audited by a third party.
* **Optimised for mobile platforms:** For example, a library with a cryptographically secure pseudorandom generator should not depend on mouse clicks ([example explained](https://www.cossacklabs.com/blog/crypto-wallets-security/#dependency-issues-with-crypto-wallets)).
* **Easy-to-use API:** The library has well-documented APIs that work the same on iOS and Android.
* **Licence:** Pay attention to the open-source licence, as not all open-source libraries are free to use.
* **Tests:** Make sure the library has unit and integration tests, especially if it deals with cryptography or operates highly sensitive data.

Research [React Native libraries](https://www.cossacklabs.com/blog/react-native-libraries-security/) and their dependencies before using them for security-sensitive functionality.

## 4. Seven steps to secure React Native app

Find your way to a secure React Native app, by following the steps that we singled out to simplify this journey:

1. Understand the implication of adding one more vendor (Facebook) and put **trust** in the security of its platform.
2. Make sure your team has enough **security expertise** for iOS, Android, and React Native. Depending on data sensitivity, you may want to hire external security experts.
3. **Educate your development team** about security best practices, secure coding, possibilities to automate security checks, OWASP [Mobile Top-10](https://owasp.org/www-project-mobile-top-10/), and [OWASP MAS](https://mas.owasp.org/).
4. **Creating security controls for mobile apps** as React Native apps are still mobile apps. Use OWASP MAS as a main guidance. Add security controls specific to React Native, if needed.
5. **Managing dependencies** in your React Native apps, and keeping them up to date. Automated dependency analysers and code scanning is a good proactive approach.
6. **Cover security controls with tests**, especially if they deal with cryptographic operations, Secure Enclave, and StrongBox Keystore
7. **Send the app for security review** by third-party experts. Implement mitigations, cover them with tests, and add the issue to the regression testing checklist.

Securing React Native mobile apps requires a holistic approach, applied to all aspects of the development process, from choosing secure libraries to implementing security controls.
