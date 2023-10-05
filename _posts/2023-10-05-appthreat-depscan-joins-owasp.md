---

date: 2023-10-05 00:00:00-0700
categories: blog
author: Prabhu Subramanian
author_image: /assets/images/people/prabhu-s.jpg
layout: blogpost
title: AppThreat dep-scan is now OWASP dep-scan
excerpt_separator: <!--more-->

---

We are super excited to announce a free open-source dependency audit tool, [OWASP dep-scan](https://owasp.org/www-project-dep-scan/). The project enables auditing the software supply-chain dependencies, container images, and operating system for known vulnerabilities, and advisories. Special thanks to [AppThreat](https://appthreat.com) for donating the project.

<!--more-->

## Tuned and Ready to use

OWASP flagship projects such as Dependency-Track, Dependency Check are used by organizations worldwide to secure the software supply-chain. dep-scan adds to the arsenal of tools by:

- integrating with OWASP CycloneDX Generator ([cdxgen](https://github.com/CycloneDX/cdxgen)) for effortless scanning of polyglot and mono-repo applications and services
- including prioritization logic to make the results actionable for developers and AppSec
- generating results in OWASP CycloneDX VDR/VEX format for easy third-party integration

A [single](https://github.com/owasp-dep-scan/dep-scan#single-binary-executables) command invocation is often enough to [integrate](https://github.com/ngcloudsec/images-info/blob/main/.github/workflows/build.yml#L27) and get the exact results in the CI/CD workflow.

## Licensed to thrill

dep-scan and the [vulnerability database](https://github.com/AppThreat/vulnerability-db) is licensed under the OSI-approved MIT license to encourage enterprise adoption and bundling.

## Future Releases

The project team led by [Prabhu Subramanian](https://github.com/prabhu) and Caroline Russell has plans to add the following features over the coming releases.

- Reachability and Exploitability Analysis to automate VEX generation
- OASIS CSAF VEX Support
- Many more

Go ahead, and give this project a scan!
