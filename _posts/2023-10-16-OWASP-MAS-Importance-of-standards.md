---

date: 2023-10-16 00:00:00-0700
categories: blog
author: Carlos Holguera
author_image: /assets/images/people/leader_carlos_holguera.jpg
layout: blogpost
title: "The Importance of Following Industry Standards: A Closer Look at OWASP MASVS in Mobile App Security"
excerpt_separator: <!--more-->

---

In cyber security staying ahead of potential threats and vulnerabilities is key; adherence to industry standards is not just a best practice; it's a necessity. In this article, we will explore why it's crucial to follow an industry standard like the [OWASP Mobile Application Security Verification Standard (MASVS)](https://mas.owasp.org/MASVS/), both from the perspective of those developing tools and services to assess mobile apps and those seeking compliance.

<!--more-->

## The Benefits of Industry Standards

- **Comprehensive Coverage, Consistency and Reliability**: Thanks to industry standards like the OWASP MASVS, which provide comprehensive coverage of the attack surface, testing remains consistent and reliable over time, instilling trust in the quality of vendor services.
- **Up-to-Date Security**: Standards like OWASP MASVS are backed by a large community of security professionals who ensure that any new threats, or best practices are quickly integrated into the standard, keeping it relevant and effective.
- **Transparency and Scope**: Established standards promote transparency in the testing process, allowing customers to clearly understand the scope and coverage, preventing hidden gaps in security assessments.
- **Trust, Credibility, and Compliance**: Vendors adhering to recognized industry standards demonstrate professionalism, build trust, and simplify compliance efforts for organizations, ensuring credibility in delivering high-quality services.
- **Improved Vendor Evaluation**: When comparing different vendors, having a known standard as a reference point makes it easier to evaluate the quality and scope of their services. It provides a common benchmark to assess their capabilities.
- **Proactive Risk Management**: By testing mobile apps against recognized standards, organizations can proactively manage and identify vulnerabilities early in the development lifecycle, minimizing the risk of costly post-release fixes.


## The OWASP MAS Project and Its Standards

The [OWASP Mobile Application Security (MAS)](https://mas.owasp.org/) flagship project provides a robust security standard for mobile apps, known as the OWASP MASVS, along with a comprehensive testing guide, the [OWASP MASTG](https://mas.owasp.org/MASTG/) as well as the [OWASP MAS Checklist](https://mas.owasp.org/checklists/). These resources cover the processes, techniques, and tools used during a mobile app security test, ensuring consistent and complete results.

![The OWASP MAS Resources](/assets/images/posts/owasp-mas-importance-of-standards/owasp_mas_resources.png)

### Comprehensive Coverage

The OWASP MASVS standard is divided into various groups of security controls, representing critical areas of the mobile attack surface, including:

- **MASVS-STORAGE**: Secure storage of sensitive data on a device (data-at-rest).
- **MASVS-CRYPTO**: Cryptographic functionality used to protect sensitive data.
- **MASVS-AUTH**: Authentication and authorization mechanisms used by the mobile app.
- **MASVS-NETWORK**: Secure network communication between the mobile app and remote endpoints (data-in-transit).
- **MASVS-PLATFORM**: Secure interaction with the underlying mobile platform and other installed apps.
- **MASVS-CODE**: Security best practices for data processing and app maintenance.
- **MASVS-RESILIENCE**: Resilience to reverse engineering and tampering attempts.

### A Standard Backed-up by Standards

The OWASP MASVS is intricately intertwined with various industry standards, underpinning its robustness and effectiveness. For instance, 

- **MASVS-CRYPTO** relies on [NIST.SP.800-175B](https://csrc.nist.gov/pubs/sp/800/175/b/r1/final) and [NIST.SP.800-57](https://csrc.nist.gov/pubs/sp/800/57/pt1/r5/final), which provide established cryptographic guidelines and assurance, ensuring that sensitive data within mobile apps remains secure.
- **MASVS-AUTH**, while the standard comprehensively covers app-side authentication and authorization, it recognizes the importance of validating security on the remote endpoint, referencing industry standards like the [OWASP Application Security Verification Standard (ASVS)](https://owasp.org/www-project-application-security-verification-standard/).
- **MASVS-CODE** encourages developers to follow best practices from [OWASP Software Assurance Maturity Model (SAMM)](https://owasp.org/www-project-samm/) and [NIST.SP.800-218 Secure Software Development Framework (SSDF)](https://csrc.nist.gov/pubs/sp/800/218/final) to prevent vulnerabilities during development.
- **MASVS-PRIVACY** draws inspiration from essential privacy regulations like GDPR, COPPA, CCPA, and ENISA, providing a foundation for privacy considerations.

Additionally, the incorporation of [NIST OSCAL](https://pages.nist.gov/OSCAL/) further enhances the OWASP MASVS ecosystem. It standardizes the testing process, allowing the selection of specific standards and profiles for compliance, and providing a structured approach to express compliance evidence and testing results. This streamlines the testing methodology and facilitates transparency and understanding among all stakeholders. This integration not only ensures consistency but also future-proofs the standard's adaptability and relevance, making it an invaluable resource for mobile app security.

## Conclusion

The importance of following industry standards like the OWASP MASVS in mobile app security cannot be overstated. It ensures consistency, comprehensiveness, and up-to-date protection against evolving threats. For vendors and customers alike, adherence to these standards is not just a matter of trust; it's a strategic choice that enhances security, credibility, and long-term cost-effectiveness in an increasingly mobile-centric world. So, choose your mobile app security provider wisely, and together, let's build a more secure mobile future.


## Resources

- OWASP Mobile Application Security - <https://mas.owasp.org/>
- OWASP MASVS - <https://mas.owasp.org/MASVS/>
- OWASP MASTG - <https://mas.owasp.org/MASTG/>
- OWASP MAS Checklist - <https://mas.owasp.org/checklists/>
- OWASP ASVS - <https://owasp.org/www-project-application-security-verification-standard/>
- OWASP SAMM - <https://owasp.org/www-project-samm/>