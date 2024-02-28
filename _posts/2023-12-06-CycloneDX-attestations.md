---

date: 2023-12-06 00:09:00-0700
categories: blog
author: Kayla Heard-Rising
author_image: /assets/images/people/kayla-heard-rising.jpg
layout: blogpost
title: CycloneDX v1.6 Introduces Support for Attestations of Compliance with Any Standard, Improving Compliance and Scalability for Consumers and Vendors of Third Party Software
excerpt_separator: <!--more-->

---

**Requiring Proof of Compliance: In the Real World, Scale Escalates Quickly.**

Almost every organization must wrestle with security compliance for their software. There are standards, policies, and guidelines from every conceivable source: government agencies, industry groups, open-source foundations, international organizations, and other standards bodies.

<!--more-->
The entire process is paper-based.  Standards are typically PDF documents and require custom written evidence, all of which defies automation and requires extensive manual effort.  The CycloneDX Attestation Project is tackling this challenge by creating “compliance as code.” We intend to dramatically increase organizations’ ability to automate the compliance process by providing machine-readable formats for:

* Capturing security requirements
* Making claims against those requirements
* Capturing evidence to support claims
* Signing the attestations

Exchanging, validating, and signing attestations of compliance may seem simple in the context of a single relationship between vendor and consumer:

<img src="/assets/images/posts/cdx-attestations/image2.png" style="float:none; width:100%; max-width:100%; margin:0; border:0" alt="">

However, when scaled up to account for multiple third-party dependencies in an organization's ecosystem, the need for standardization in managing and maintaining attestations of compliance becomes apparent for both software vendors and consumers.

<img src="/assets/images/posts/cdx-attestations/image1.png" style="float:none; width:100%; max-width:100%; margin:0; border:0" alt="">

Considering that software vendors likely have multiple products, each with multiple customers – and considering that software consumers likely rely on multiple third-party products to maintain critical operations in their organization – the impact of creating and consuming attestations of compliance across B2B transactions escalates quickly.

<img src="/assets/images/posts/cdx-attestations/image5.png" style="float:none; width:100%; max-width:100%; margin:0; border:0" alt="">

If each consumer set their own requirements for receiving attestations and evidence of compliance, or each vendor set their own standards for providing proof of attestation, significant inefficiency is added to the process of exchanging attestations. Consumers may take additional time to verify and adjust to unfamiliar attestation and evidence formats, while vendors may need to adjust their attestations and evidence to meet consumers’ requirements.

Committing to producing and consuming attestations of compliance introduces three key pain points:

### Multiple levels of dependencies, or transitive dependencies
With so many details and requirements in each individual standard, how might consumers be alerted when third party software falls out of compliance via one of the vendor’s external dependencies? Furthermore, if a vendor does fall out of compliance due to a vulnerable transitive dependency, how might they demonstrate that they are back in compliance and therefore regain the trust of their customer?

Given that many consumers rely on multiple third-party software solutions for critical operations, it requires keen oversight to ensure that every one of those vendors remain in compliance to the level of transitive dependencies.

### Attestation management at scale
Imagine a situation in which a consumer requires all vendors to comply with the same standard as a requirement for purchasing their product. Without a common attestation format, a company purchasing third-party or enterprise software solutions may have to read through as many different versions of attestations and evidence as they have vendors.

How might consumers of third-party software keep from being overwhelmed by reading and evaluating proof of attestations for each individual product they utilize, and continue doing this each time one of those vendors makes a change that might introduce a vulnerability? Is there a consistent way for consumers to know, at a glance, what standards the software is compliant with and to what degree, and even better, obtain this information in a way that is consistent across all the software they consume so that they do not need to adapt to different attestation and evidence formats for every software package they validate?

This is a particularly acute need for standards that heavily focus on policies and procedures, as attestation would either require manual entry of evidence or extensive integrations to automate. 

### Burden of proof for an entire portfolio
Generating proof for the attestation of a single product may be a straightforward documentation task before go-to-market. Generating proof for attestations across an entire product portfolio, with updates on every release that may affect compliance, is an exponentially more complex task that requires standardization and process to prevent it from becoming cost-preventive or blocking the release and sale of products.

Standardization of attestation formats and clearly readable links between the product requirements, the product’s degree of compliance, and the vendor’s proof of compliance can help to quickly resolve concerns about a product’s compliance with a necessary standard. Without standardization, if a buyer requires more proof of compliance or does not accept a vendor's standard proof of attestation, additional effort would be required for the vendor to understand the gap in documentation, go back to engineers to document the required technical information, and coordinate with stakeholders to craft a new proof of attestation for the buyer.

Lockheed Martin, a member of the CycloneDX Industry Working Group, faced this risk due to the sheer size of their product portfolio. With thousands of products being manufactured for use by government agencies, all of whom would require attestation of each product’s compliance with NIST’s Secure Software Development Framework, they needed a way to optimize the generation and management of attestation documents. Lockheed Martin has partnered with the CycloneDX community on attestation support to forge a path forward for organizations with similar needs:

> _“Lockheed Martin has collaborated with other members of the OWASP community to develop CycloneDX 1.6 attestation and standards support to meet requirements outlined in President Biden's Executive Order on improving the nation's cybersecurity (EO 14028). Our work on CycloneDX enables us to deliver software bill of materials using open standards for interoperability with our public sector partners and customers. Lockheed Martin’s collaboration on CycloneDX 1.6 provides a path to automating policy to implementing NIST’s Secure Software Development Framework as part of the Office of Management and Budget Memorandum M-22-18.”_
>
> **-Ian Dunbar-Hall**
>
> **Lockheed Martin Software Factory Chief Engineer**

## CycloneDX Makes Attestation Manageable for Everyone in the Equation
The CycloneDX Attestations Working Group is excited to announce support for attestations of compliance with **any standard**, which will be released with CycloneDX version 1.6. This was made possible due to the partnership between CycloneDX contributors and members of the CycloneDX Industry Working Group.

At launch, the CycloneDX v1.6 standard will have pre-filled compliance requirements for several standards, including OWASP SCVS, ASVS, and MASVS, as well as the NIST Secure Software Development Framework for the convenience of vendors who work with the federal government. However, users can also enter and link to the requirements for other standards, even those for policies and procedures internal to their company. CycloneDX Attestations ties together the standard, the compliance status, and the related evidence in a way that is simple enough to be understood at a glance, while also flexible enough to be adapted for any standard:

<img src="/assets/images/posts/cdx-attestations/image4.png" style="float:none; width:100%; max-width:100%; margin:0; border:0" alt="">

This supports all user personas in B2B transactions:
* Software vendors have an established template for providing attestation of full compliance with any standard, or partial compliance with expected milestones to reach full compliance.
* Software vendors with third party dependencies can check to see if a dependency is putting them out of compliance with any standards required by their customers.
* Consumers have an easier time parsing through potentially lengthy attestation evidence; an SBOM provides not only a structured and familiar format that links evidence to requirements, but provides the opportunity to develop tools for automatically processing attestation evidence and displaying a result readable to non-technical stakeholders.
* Vendors will be able to automate internal audits of compliance with NIST or other standards.
* Buyers will likewise be able to automate routine audits of their third party software’s compliance with NIST or other standards, opening up the opportunity for more frequent auditing and vulnerability detection. 

Default support for NIST, SCVS, and ASVS/MASVS standards can also be chained together to create a strong starting point for a vendor that is just starting to experiment with attestations of compliance. The Attestation of Compliance section can provide evidence that the product complies with individual sections of the NIST requirements (with support for multiple sources of evidence for a single requirement), while proof of SCVS, ASVS, and MASVS compliance speak to the quality of all other attestations; showing that the company is oriented toward security and documenting proof in a thorough fashion.

All of these combined factors benefit both consumers and vendors of B2B software. Consumers can make informed decisions when evaluating multiple options for software vendors, being able to more easily determine which is the most verifiable secure. Vendors can proactively identify gaps in their compliance or evidence of compliance, giving them an opportunity to remediate this rather than be caught unaware during sales negotiations or onboarding of a new customer.

## How to Use CycloneDX Attestations – What This Looks Like for CycloneDX Adopters
When both vendors and consumers utilize the same standard for submitting proofs of attestation – especially a standard which is familiar, easy to generate, and easy to consume – the ecosystem of exchanging third-party software solutions becomes far more manageable, whether for B2B transactions or open-source projects.

Here is an example workflow for a CycloneDX user filling out an attestation of compliance:

<img src="/assets/images/posts/cdx-attestations/image3.png" style="float:none; width:100%; max-width:100%; margin:0; border:0" alt="">

## With the Community's Help, Ensuring Compliance with Security Standards through Attestation can be an Easy, Standard Part of B2B Transactions
At present, the Attestations section of the CycloneDX standard is machine-writable and machine-readable, but tools are still needed to automate the population and consumption of attestations in existing software products.

These are some of the more prevalent user needs which could potentially be met by tools created by the community:
* Populating the SBOM with standard requirements based on user input or attached files.
* Parsing through the attestations section of the SBOM and translating this into a human-readable result of "compliant”, "partially compliant", or "not compliant".
* Providing a UI for non-technical stakeholders to manually set compliance levels or attach evidence outside of editing the JSON/XML objects of the SBOM itself.

### Why tools are needed to generate attestation documents
While many fields in a CycloneDX SBOM can be automatically generated as part of the build process, many NIST and ISO standards involve non-technical requirements for policies and procedures. (Example: A standard may require proof that employees undergo yearly cybersecurity training.) 

The proof for non-technical requirements may be present in a number of different tools with the capability for API integration, but there is a definite need for tools which are capable of integrating with these endpoints and populating the SBOM with attestation evidence.

Filling out a nested JSON object by hand may also be more difficult for non-technical stakeholders if this is not a format they do not work with regularly. As a result, there is also a need for attestation tools which provide a user interface for individuals to fill out standard requirements, attest to their degree of compliance, and attach evidence for each standard’s requirements.

## Why tools are needed to read attestation documents at scale
Attestation data is contained in nested JSON or XML objects within a CycloneDX Software Bill of Materials (SBOM), conferring a significant advantage: CycloneDX Attestations are machine-readable. In other words, it becomes possible to build tools that instantly parse through lengthy attestations and bodies of evidence for dozens if not hundreds of products; surfacing an easy-to-read synopsis to the end user.

If built, these tools would exponentially reduce the time for security professionals or project managers to validate attestations, making the exchange of attestation statements a fast, easy part of B2B transactions.

## Get involved with CycloneDX
The OWASP CycloneDX community is always looking for new members who are interested in getting involved and supporting new and innovative uses for SBOM. Anyone who would like to provide feedback, contribute ideas, or create tools is welcome to join the CycloneDX Attestations Working Group.

For more information on CycloneDX milestones, go to [https://cyclonedx.org/news/](https://cyclonedx.org/news/).

CycloneDX has a rich community of contributors, supporters, and adopters helping each other to drive innovation and change. [It is quick and easy to join](https://cyclonedx.org/about/participate/), and all new participants are welcome.
