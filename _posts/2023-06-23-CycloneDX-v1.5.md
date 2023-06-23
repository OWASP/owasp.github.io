---

date: 2023-06-23 00:00:00-0700
categories: blog
author: Kayla Heard-Rising
author_image: /assets/images/people/kayla-heard-rising.jpg
layout: blogpost
title: How CycloneDX v1.5 Increases Trust and Transparency in More Industries
excerpt_separator: <!--more-->

---

OWASP is often the first to reveal new, innovative ways to leverage SBOM. The release of CycloneDX version 1.5 is no different, opening up SBOM adoption to new industries and introducing numerous ways to customize CycloneDX SBOMs to indicate quality, show transparency, and expedite vulnerability remediation while increasing trust in the supply chain.

<!--more-->

CycloneDX v1.5 further expands visibility and security benefits to new industries through generation of xBOMs: the concept of a CycloneDX BOM is not just restricted to software, but capable of conferring the same benefits to hardware, operations, manufacturing, and many more applications.

For example, SaaSBOM, or a Software as a Service BOM, provides an inventory of services, endpoints, and data flows/classifications that power cloud-native applications. Hardware Bill of Materials, or HBOM, supports documentation of components, devices, firmware, configurations, and many other fields that make it ideal for producers of consumer electronics, IoT devices, and embedded devices. CycloneDX xBOMs can also be combined to represent a product ecosystem. For a full-stack product offering, a company can generate an HBOM for devices in the field and a SaaSBOM for the software components of each service.

With version 1.5, CycloneDX introduces new xBOM types that support both new areas in the product ecosystem for existing users, and also makes CycloneDX usage feasible for new industries altogether.

## CycloneDX Increases Transparency and Trust in Machine Learning, Manufacturing, and Low Code Application Platforms
CycloneDX v1.5 is the first and only format to support three new xBOM types: Machine Learning Bill of Materials (ML-BOM), Manufacturing Bill of Materials (MBOM), and SBOM for Low Code Application Platforms. In the near future, vendor AquaSecurity will also introduce support for Kubernetes Bill of Materials (KBOM), a new type of xBOM based on the CycloneDX v1.5 format.

In each of these industries, trust in the product is critical. Whether purchasing a new smart appliance or subscribing to a website builder, a buyer wants to feel assured that their data will stay secure, be informed of how their data is being used, and know that the product they receive is providing reliable, high-quality information. A CycloneDX SBOM provides not only the dependencies, components, and processes that transform a product or data set – but also the presence, impact, and risks associated with that product.

### Machine Learning Bill of Materials (ML-BOM)
Machine Learning Bill of Materials (ML-BOM) includes documentation of an algorithm’s model and dataset, enabling its creator to provide contributors with assurance of security and privacy, and consumers with transparency on safety and ethical considerations. Even if the SBOM is not publicly distributed, it can serve as a “snapshot” that an organization or creator can refer back to when reassuring contributors that their data is being stored securely and privately, or making consumers aware of the model’s methods and constraints for learning.

### Manufacturing Bill of Materials (MBOM)
Manufacturing Bill of Materials (MBOM) describes how a product is made, improving upon the concept of a traditional Bill of Materials (BOM). While both document the materials and sources needed to manufacture a product, and both can be used to manually document and identify risks in a supply chain, CycloneDX also documents how a product combines hardware, firmware, software, processes, and testing to create the final product distributed to the customer. This serves as a record of **provenance**, or the history of the origins and ownership of a product and how it was built. This can reveal potential security compromises or weaknesses in the toolchain, or the product’s ecosystem and the code, components, and processes that enable this.

CycloneDX has **doubled the number of external references supported in all SBOMs and significantly increased the types of components supported** in version 1.5, allowing for a greater degree of documentation and linking than ever before. This expands CycloneDX’s capability to identify vulnerabilities by adding fields that describe risk assessments, threat models, and the outputs from security tools. 

### Low Code Application Platforms
CycloneDX is introducing the ability to generate SBOMs for Low Code Application Platforms, which are development environments used to create application software through a graphical user interface instead of traditional hand-coded computer programming. Such platforms reduce the amount of traditional hand-coding, enabling accelerated delivery of business applications. Individuals or businesses often outsource key parts of their daily operations, such as e-commerce, scheduling, or contact forms, to these platforms in exchange for a subscription.

Generating a CycloneDX SBOM allows developers writing Low Code Applications to assure their users that their data is secure. In addition, Low Code Platform vendors can now enable SBOM generation from their respective platforms, enabling users who create applications or processes on a Low Code Platform to dynamically receive SBOMs of their own application.

### Kubernetes Bill of Materials (KBOM)
Following the release of CycloneDX v1.5, users of AquaSecurity's [Trivy](https://aquasecurity.github.io/trivy) tool will be able to generate a new type of xBOM: Kubernetes Bill of Materials (KBOM).

KBOM documents the composition of a Kubernetes cluster, creating a manifest of the components, versions, and images within. This affords transparency to software teams who have used a third-party tool or provider to set up and configure their Kubernetes cluster, providing a comprehensive inventory of a cluster's control plane components, node components, add-ons, and storage types. With this information in hand, software teams can conduct a vulnerability assessment of the components within a Kubernetes cluster, revealing potential threats to the underlying infrastructure of an organization’s software stack. KBOMs can be generated for an existing cluster or as part of the installation and configuration process, using the Kubernetes API to discover the cluster.

## CycloneDX Creates a Foundation of Trust with Enhanced SDLC and SAM Support
CycloneDX v1.5 adds new fields related to Software Development Lifecycle (SLDC) and Software Asset Management (SAM), which provide further context to how the SBOM was generated, the accuracy of the data contained within an SBOM, and the nature of an organization’s dependencies on third-party software components. Data in these fields can be used to increase stakeholder confidence in the product security communicated by the SBOM.

### CycloneDX v1.5 Provides the Most Advanced Licensing Support of Any SBOM Format
In addition to the comprehensive open-source license support conferred by previous versions, CycloneDX v1.5 adds **commercial license support**, which enables users to document the license, licensee, licensor, license number, license type, purchase order, renewal date, and expiration date for any dependent component in their project. With a CycloneDX SBOM, users have one central place to see all the licenses they use, where licenses may be missing, and when to renew or replace licenses to keep their product distribution up and running.

As a product’s lifecycle matures and third-party components transition from planned integrations into actual integrations, CycloneDX users can leverage new fields introduced by version 1.5 to support Software Asset Management (SAM). While the Software Development Lifecycle (SLDC) typically uses tools for open-source license compliance, SAM is more focused on commercial license support and procurement. Documentation of SAM lifecycles is frequently required for enterprise solution adoption among Fortune 500 companies. In addition, storing license data in a CycloneDX SBOM normalizes data for licensing, configurations, renewals, and deployments for software and hardware assets, providing a springboard for organizations to digitally transform their procurement and SAM processes.

### OWASP Introduces Comprehensive SBOM Quality Indicators in CycloneDX
CycloneDX v1.5 lifecycle and evidence fields not only indicate the quality of a product, but also trustworthiness of the product’s SBOM itself. OWASP recommends five dimensions of SBOM quality:

- **Breadth** - the coverage in the types of data represented in a BOM
- **Depth** - the amount of detail or difficulty needed to represent data within a BOM
- **Lifecycles** - the number of lifecycles or the favorability of specific lifecycles in the creation of a BOM
- **Techniques** - the approaches used to determine component identity
- **Confidence** - the confidence of individual techniques, and the analysis of the sum of all techniques used to identify components

To date, CycloneDX is the only SBOM format that includes data supporting all five dimensions. 

### SDLC and SAM Support - Communicating Product Quality and Breaking Down Barriers to Product Adoption
Version 1.5 introduces support for SDLC fields, which communicate the quality of the SBOM by identifying the stage of the product lifecycle in which it was generated. SBOMs created early on in the lifecycle can provide more insight into the planning, decision-making, and quality improvements of the product as it matures.

SBOMs created early on in a product’s lifecycle capture the planning process for components and services that may be used. As the product progresses through the phases of its lifecycle, the SBOM is further populated with source materials, development artifacts, dependencies and components, component source data, build processes, operational status, configurations, potential security issues, and/or lack of security issues. 

These add to CycloneDX’s existing benefits to SDLC planning by:
- Creating a snapshot of dependencies, vulnerabilities, changes, and licenses when SBOMs are generated at points throughout the product’s lifetime.
- Revealing additional needs for planning or changes during the early lifecycle, especially in regard to licensing and security issues.
- Showing how development teams pivot on risk throughout the product’s lifecycle, removing unnecessary or vulnerable components while retaining those critical to its functionality.
- Assisting in the discovery stage of the lifecycle by helping teams discover projects already in operation and the software/hardware assets they utilize.
- Assisting in the decommission stage of the lifecycle by providing a list of all components that need to be taken offline with a product, reducing unexpected cost and risk for the organization.

## CycloneDX Reduces Time to Action on Vulnerability Investigation and Software Composition Analysis
There are three things that can soften the impact of unexpected work: advance preparation, early detection, and the ability to take immediate action. Fortunately, CycloneDX v1.5 introduces a diverse new array of fields to assist with this.

### Preparing for the Worst - Using CycloneDX to Document the Software Development Life Cycle
Using a CycloneDX SBOM to document SDLC planning lays the groundwork for time savings during future Software Composition Analysis (SCA) and/or vulnerability fixes. This will save SCA professionals or members of a software development team countless hours in going back through artifacts to pinpoint the origin and history of a given vulnerability, affording everyone more time and energy to focus on problem-solving.

### SCA and Vulnerability Investigation - CycloneDX Surfaces Critical Information
CycloneDX v1.5 adds 3 capabilities which are critical time-savers to investigating the real-world risk and impact of vulnerabilities within a project:

- **Identity Evidence** - proves the identity of a component and its source, improving confidence in the accuracy of the SBOM and the techniques used to determine component identity.
- **Occurrences** - shows where individual instances of a component are located in the source code for a project, and aggregates those instances into a single component.
- **Call Stack** - similar to a stack trace, this identifies if a vulnerable component was called by the application and shows where it was invoked in a nested function call, indicating the reachability of the vulnerable component and what data or functionality may have been impacted. (This field is particularly useful for IAST vendors.)

Version 1.5 also adds support for **proof of concept data** on vulnerabilities, which enables software teams to document and demonstrate how a vulnerability could theoretically be exploited. This may include proof of the exploit happening, payloads to trigger the exploit, code for remediation, and additional details on remediation plans. CycloneDX documentation of vulnerability proof-of-concepts saves time on explanation, investigation, and execution when it is time for a vulnerability to be patched, and can serve as documentation of when and why the vulnerability will be patched. This is commonly used for responsible disclosure, which is a transparency and trust measure to make stakeholders aware of existing vulnerabilities when adopting a product.
