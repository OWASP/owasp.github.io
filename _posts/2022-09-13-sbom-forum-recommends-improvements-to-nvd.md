---

date: 2022-09-13 00:00:00-0700
categories: blog
author: Steve Springett
author_image: /assets/images/people/leader_springett.png
layout: blogpost
title: New Recommendations to Improve The NVD
excerpt_separator: <!--more-->

---

New recommendations drafted by members of OWASP, The Linux Foundation, Oracle, and others, aim to improve the 
accuracy of the NVD with a focus on modern, automated use cases. The group, informally named the "SBOM Forum", is led by
supply chain consultant and blogger, [Tom Alrich](https://www.linkedin.com/in/tom-alrich-6314055/). Their first paper 
titled [A Proposal to Operationalize Component Identification for Vulnerability Management](/assets/files/posts/A%20Proposal%20to%20Operationalize%20Component%20Identification%20for%20Vulnerability%20Management.pdf).
recommends that MITRE and the NVD adopt Package URL for the identification of open source and commercial software along
with multiple GS1 standards for hardware. In doing so, the accuracy of vulnerability management can be dramatically
improved while increasing the efficiency and effectiveness of the teams doing it.

<!--more-->

### Background
The National Vulnerability Database (NVD) is the essential source of vulnerability intelligence which the infosec 
industry depends on. In the early days of the NVD, users had to read vulnerability descriptions to determine if they 
were impacted. The adoption of the Common Platform Enumeration (CPE) changed all this. With CPE, automation could 
finally be achieved. CPE provides a simple way to identify the vendor, product, and version of components and includes 
support for identifying applications, operating systems, and hardware devices. CPE has evolved over the years to 
represent additional forms of data, but the general premise remains unchanged. With CPE, users could finally query the 
NVD with product information to determine if those products had known vulnerabilities.

### The Challenge
CPE has many faults. It’s a centralized solution containing a product dictionary maintained by humans which precisely 
describes the names of vendors and products. In the early days of the NVD, this solution worked well. The emergence of 
package managers and the explosion of open source has dramatically changed the landscape for which CPE was originally 
designed.

With package managers, the author of the package is responsible for its name and version. It’s a decentralized model 
unlike CPE. As such, it’s much more scalable and precise. For precision, let’s take a look at two examples.

### Example 1

<div class="article-table"></div>

| Field       | CPE   | Package Manager        | 
| ----------- |-------|------------------------|
| **Vendor / Namespace** | apache | org.apache.logging.log4j |
| **Name**   | log4j | log4j-core |
| **Version**  | 2.0   | 2.0 |


In the case of log4j, the vendor defined by the CPE does not match how the project self-identifies. The same holds true
for the name. However, log4j consists of multiple modules with only `log4j-core` being affected by the Log4Shell 
vulnerability. Other modules such as `log4j-api` are not affected, however the CPE does not provide the level
of granularity needed to make this determination. 

### Example 2

<div class="article-table"></div>

| Field       | CPE         | Package Manager | 
| ----------- | ----------- | --------------- |
| **Vendor / Namespace** | redhat | org.jboss.resteasy |
| **Name**   | resteasy | resteasy-jaxrs |
| **Version**  | 3.1.0 | 3.1.0-Final |


When developers use the `resteasy-jaxrs` package, they reference the namespace, name, and version as identified by the
package manager. All modern ecosystems created in the last 20 years use the same approach. However, when users need to
query the NVD to determine if there's a vulnerability in this package, there's a few challenges that prevent them from 
doing so:

1. There are three fields that the author of this package has specified. All three fields are inaccurate in the NVD, likely a result of human intervention required to maintain the CPE dictionary. There's a clear disconnect between what the NVD calls the package and reality.
2. Like the log4j example above, Resteasy is a multi-module project, the `resteasy-jaxrs` module is just one of the available libraries. The CPE does not describe the module, it describes the "product" thus requiring a human to read the vulnerability description to determine if the jaxrs module is affected or not.

With these limitations, the NVD has largely become unusable in an age of hyper-automation and explosive growth in open 
source software. Left unchanged, the relevance of the NVD will continue to diminish. For the past decade, alternative 
sources of vulnerability intelligence have emerged, many of which are Software Composition Analysis (SCA) vendors. 
Many SCA vendors have built their own vulnerability databases with accurate mappings to software packages. SCA vendors 
have played a pivotal role as their solutions have provided a workaround for limitations in the NVD.

### The Vision
No, we are not solving the "naming problem". But the SBOM Forum recommends a few simple changes which, if implemented
by MITRE and the NVD, could propel the NVD forward.

The recommendations are to:

* Support Package URL - This will handle both open source packages and commercial software.
* Support GS1 standards (GTIN and GMN specifically) for hardware devices. 

If these changes are implemented, users would be able to:

* Query the NVD directly using the native package coordinates or purl of the software and receive accurate vulnerability information. No CPE fuzzy matching required.
* Query the NVD using the UPC label (or similar hardware identifier) on the back of a device to obtain accurate vulnerability information. No need to lookup vendors in the CPE dictionary.

### How to Help
I have met with researchers at MITRE, and have a follow-up call scheduled later this week to answer remaining questions.
The U.S. [Cybersecurity & Infrastructure Security Agency (CISA)](https://www.cisa.gov/) plans to seek public feedback 
in the future. If you or your organization is in favor of these changes, your public support could help turn these 
recommendations into reality.

The first step is getting support for Package URL and GS1 standards into the [CVE schema](https://github.com/CVEProject/cve-schema). 
Voting and commenting on two GitHub tickets is a great way to get involved. The tickets are:

* [Support PURL as identifier](https://github.com/CVEProject/cve-schema/issues/173)
* [Add support for GS1 (GTIN and GMN) identifiers](https://github.com/CVEProject/cve-schema/issues/194)

<style>
    .article-table + table { 
        width: 100%;
        margin-bottom: 2rem;
    }
</style>