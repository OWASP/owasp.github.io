---

date: 2024-03-07 00:09:00-0700
categories: blog
author: Olle E. Johansson
author_image: /assets/images/people/Olle-E-Johansson.jpg
layout: blogpost
title: OWASP CycloneDX is ready to support your CRA compliance journey!
excerpt_separator: <!--more-->

---

_Software development aimed at selling products in the European Union will soon change forever. Regardless of whether the product is an IoT device, a child's toy with embedded software, a server-side application, or a mobile app - the software will have to be marked with the CE symbol, which will include cybersecurity aspects on the product. At the heart of the new regulation, the EU Cyber Resilience Act, is the software bill of materials (SBOM). OWASP CycloneDX stands well prepared with specifications of bill-of-materials and an arsenal of tools that will help manufacturers in their compliance process._

<!--more-->

## Cybersecurity as a lifecycle process - not as a gateway before release

The EU Cyber Resilience Act (CRA) aims to add cybersecurity requirements during the lifetime of a product. Manufacturers
selling products on the EU market must deliver free security upgrades during the product’s lifetime. They will also have
reporting requirements to the authorities if there are known attempts to use a vulnerability in the product for an attack.
In order to manage vulnerabilities in the product’s dependencies - commercial and open source tools and libraries used to
build the product - the CRA requires manufacturers to create a software bill of materials (SBOM). The idea is for the 
manufacturers to use this to regularly check for vulnerabilities and upgrade dependencies to stay secure. In addition, 
the source code produced by the manufacturer has to be secure by default and secure by design. OWASP has a number of 
resources to aid in secure design, including the [OWASP Application Security Verification Standard](https://owasp.org/asvs)
(ASVS), the [OWASP Software Assurance Maturity Model](https://owaspsamm.org/) (SAMM), and reference material for 
[threat modeling](https://owasp.org/www-community/Threat_Modeling) and other positive security behaviors.

## Automatic security updates during the lifetime of the product

A manufacturer will have to support not only the latest software version but also all versions used by customers. The 
security updates have to be available for up to ten years. In addition, the products will in most cases have to support 
automatic security updates, unless there are strong arguments against it. The customer may want to disable automatic 
updates but still needs information about existing updates.

This means that the manufacturer not only has to process the latest SBOM for their product, they will have to process 
the SBOM for all existing and supported releases. There are many solutions for this on the market, both commercial and 
open source. OWASP has a set of free tools that can support this process and is used by large manufacturers of software 
with thousands of products. The [CycloneDX Tool Center](https://cyclonedx.org/tool-center/) has an abundance of open 
source and proprietary tools that support the CycloneDX standard. And [OWASP Dependency-Track](https://dependencytrack.org/)
is the reference platform that consumes and analyzes SBOMs for security, operational, and license risk.

There is no requirement in the CRA itself to make the SBOM available for customers. It’s primarily a tool for the 
manufacturer to use and for the certification bodies to check compliance with.

## Software transparency before and after the purchase

The Cyber Resilience Act aims to make sure a customer can evaluate the product from a cybersecurity view before making 
a purchase. In order to do so, all vulnerability fixes have to be published publicly. The manufacturer also needs to set
up a coordinated vulnerability response process to interact with researchers, customers and partners that find issues in
the software.

CycloneDX has strong support for [Vulnerability Exploitability eXchange](https://cyclonedx.org/capabilities/vex/) (VEX) 
that will be used to communicate a vendor's assessment of vulnerabilities in the software - indicating whether a certain
vulnerability exposes a user to risk or not. It also indicates whether the software needs to be updated to fix the issue.

## Due diligence and automation between a manufacturer and upstream vendors

The CycloneDX specification and tooling assist in the relationship between manufacturers and customers and are a crucial
part of the software supply chain. The CRA will hold a manufacturer responsible for all aspects of a product, which 
means that all components have to go through due diligence and constant monitoring for upgrades, vulnerabilities, and 
known exploits. As components are sourced from both commercial vendors and open source projects - the automatic exchange
of the software transparency attestations will be needed. CycloneDX is currently working on standardizing this exchange 
and will soon bring the first versions of an API to the [Ecma TC54](https://tc54.org/) working group.

## Where does CycloneDX fit in?

CycloneDX is the leading SBOM format with years of experience. The standard work within the OWASP community is now 
augmented with the [Ecma International](https://www.ecma-international.org/) standardization in [Technical Committee 54](https://ecma-international.org/technical-committees/tc54/) (TC54). 
While keeping the community change control, the Ecma standardization will lead to a high-quality standard that fits into 
the CRA certification process.

CycloneDX covers not only the Software Bill Of Materials but also strong support for several types of bill-of-materials 
ranging from hardware to software-as-a-service and cryptography; CycloneDX supports the secure-by-design requirement 
in the CRA.

Are you ready to dive deeper into CycloneDX? Begin your journey by visiting [cyclonedx.org](https://cyclonedx.org/) and 
with the [Authoritative Guide to SBOM](https://cyclonedx.org/guides/sbom/OWASP_CycloneDX-SBOM-Guide-en.pdf)!
