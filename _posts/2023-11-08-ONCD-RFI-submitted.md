---

date: 2023-11-08 00:00:00-0700
categories: blog
author: Andrew van der Stock
author_image: /assets/images/people/staff_andrew.jpg
layout: blogpost
title: OWASP's response to the ONCD RFI on Open Source Security and Prioritization
excerpt_separator: <!--more-->

---

Today, the OWASP Foundation and its leaders [submitted a response](/assets/files/posts/Open-Source%20Software%20Security%20RFI%20Response%20-%20OWASP.pdf) to the US Government's Office of the National Cyber Director's [Request for Information on Open Source Security: Areas for Long-Term Focus and Prioritization](https://www.whitehouse.gov/oncd/briefing-room/2023/08/10/fact-sheet-office-of-the-national-cyber-director-requests-public-comment-on-open-source-software-security-and-memory-safe-programming-languages/). The response was written by OWASP's Leaders, edited by the OWASP Foundation's Executive Director, Andrew van der Stock, and reviewed by those active in our community.

<!--more-->

OWASP's [response can be downloaded here](/assets/files/posts/Open-Source%20Software%20Security%20RFI%20Response%20-%20OWASP.pdf). Some highlights include:

### OWASP's prioritization of the US Government's desire to improve the security of open source software

- Financial Support for Open-source: Secure funding is essential to sustain open-source software education and development
- Developer Education and Accreditation: Strengthen software security by providing comprehensive training and certification for developers.
- Software Supply Chain Integrity: Implement systems to help users identify and avoid insecure software components.
- Broad Vulnerability Reduction: Adopt standards like OWASP's ASVS and SAMM to eliminate widespread software vulnerabilities.
- Legacy System Security: Focus on improving memory safety in applications written in older languages like C, C++, COBOL, or Fortran.

### Secure Open Source Foundations

OWASP believes that to secure open source, funding organizations such as OWASP is critical to rolling out funding and project managing our programs that deliver on the US Government's priorities.

### Reducing Entire Classes of Vulnerabilities

OWASP believes that the OWASP Application Security Verification Standard (ASVS) and the OWASP Software Assurance Maturity Model (SAMM) are the best ways to reduce entire classes of vulnerabilities. We believe that the US Government should recommend or mandate the use of the ASVS and SAMM in software development projects, and that the US Government should help fund the development of ASVS and SAMM.

### Secure Software Development Training and Certification

OWASP believes that the US Government should fund the development of secure software development training and certification for all major programming languages, but particularly Rust and Swift, which are two of the highlighted memory-safe languages by CISA. OWASP has a huge role in setting tertiary and industry syllabuses, and accrediting vendors and universities to deliver secure software development training and certification.

### Secure Software Supply Chain

OWASP has some of the best tools - bar none - that are free, open, and available to all. We believe that the US Government should fund the development of the OWASP Dependency Check and Dependency Track tools, CyloneDX, and the Software Component Verification Standard, and recommend their use in software development projects, particularly open source projects where access to commercial tools is limited or non-existent.

### Legacy System Security

OWASP believes that migrating code or wholesale re-writing code is best served by wrapping memory sensitive portions of code, such as those written in C, C++, COBOL, or Fortran, in memory-safe languages such as Rust or Swift. We also state that most web application and API programming languages are considered safe(r) by most practitioners, and thus the focus should be on the memory sensitive portions of code.

The OWASP Foundation thanks its leaders for their contributions to this response, and we look forward to working with the US Government to improve the security of open source software.

For media enquiries, please contact [Andrew van der Stock](mailto:andrew.vanderstock@owasp.com) or at [@vanderaj](https://twitter.com/vanderaj) on X (formerly Twitter).
