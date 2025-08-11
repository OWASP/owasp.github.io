---

date: 2025-08-11 00:00:00-0700
categories: blog
author: Prabhu S. and Michael Tsfoni
author_image:
layout: blogpost
title: cdxgen and CycloneDX .NET Join GitHub Secure Open Source Fund
excerpt_separator: <!--more-->

---

# cdxgen and CycloneDX .NET participated in the GitHub Secure Open Source Fund

---

**Strengthening supply-chain security from the inside out.**

In the domain of supply-chain security, two distinct aspects exist: security within the supply chain and the security of the supply chain itself. The **CycloneDX** community, with its extensive ecosystem of open-source specifications, libraries, and tools, focuses primarily on enhancing security and transparency within the supply chain. Nevertheless, there remains a critical need to strengthen the broader security of the overall supply chain by providing open-source projects and maintainers with substantial funding, essential tools, relevant knowledge, and ongoing support.

Introducing the **GitHub Secure Open Source Fund (SOSF)**, purposefully designed to secure fast-growing dependencies critical to large projects and ecosystems. We are pleased to announce that two key projects from the CycloneDX community — **[cdxgen](https://github.com/CycloneDX/cdxgen)** and **[CycloneDX .NET](https://github.com/cyclonedx/cyclonedx-dotnet)** — have been [selected](https://github.blog/open-source/maintainers/securing-the-supply-chain-at-scale-starting-with-71-important-open-source-projects/) as proud recipients and participants of GitHub’s SOSF.

Inspired by GitHub’s AI accelerator program, SOSF provides structured training and dedicated hands-on support from experts at Microsoft, GitHub, and external consultants. With substantial personal and infrastructure sponsorships, the program enables project teams to strategically plan their long-term roadmaps.

## CycloneDX .NET

As the SBOM generator for .NET and .NET Framework projects, it enables developers to integrate SBOM creation directly into CI/CD pipelines.

Through the GitHub Secure Open Source Fund, we established key security processes and prepared the groundwork for long-term improvements:

* Drafted an Incident Response Plan to formalize response procedures
* Strengthened CI/CD pipeline security practices
* Enhanced approaches for application security and sensitive data handling in SBOM generation
* Initiated a threat model to guide ongoing risk analysis

The program provided structured expertise and strategic direction, positioning the project to better integrate SBOM generation into the .NET build process. Our next steps focus on implementing the threat model, expanding dependency transparency, and improving SBOM data quality.

## cdxgen

As a rapidly growing project with increasing adoption, it has been an honor for **cdxgen** to participate in GitHub’s SOSF program. Throughout the four-week duration, our team fully utilized the resources, models, and collective knowledge provided by the cohort to comprehensively review our project’s security and infrastructure.

In collaboration with a dedicated GitHub security success buddy, we identified five significant vulnerabilities within cdxgen. With the [release](https://github.com/CycloneDX/cdxgen/releases) of versions **11.4.x** and **11.5.x**, we not only addressed these vulnerabilities but also mitigated entire categories of weaknesses through the implementation of comprehensive allow-listing for external commands and remote hosts. This enhanced seat-belt approach to security further establishes cdxgen as the preferred tool for generating Bill of Materials (BOM) documents at scale, suitable for both trusted and untrusted projects and container images.

Maintaining cdxgen’s infrastructure is both complex and resource-intensive, with availability in over 110 executable formats and container images. It ranks as one of the top consumers of computing and storage resources within the CycloneDX community and OWASP. Thanks to significant infrastructure sponsorship from Microsoft, we aim to resolve our computing resource bottlenecks by deploying a hybrid infrastructure that includes the Azure cloud stack, self-hosted compute resources, and GitHub Actions.

Combined with existing funding from the EU, NLNet, and private organizations, cdxgen remains sustainably positioned with a clear, long-term roadmap. As an OWASP project committed to inclusivity and diversity, we actively encourage contributors from all backgrounds and skill levels to join our efforts. Additionally, our team enthusiastically supports and practices AI-driven coding methodologies (**Vibe coding**).

---

**Open source thrives when security is a shared responsibility.** With the support of the GitHub Secure Open Source Fund, both CycloneDX .NET and cdxgen are poised to continue strengthening supply-chain security — and setting new standards for transparency and trust.
