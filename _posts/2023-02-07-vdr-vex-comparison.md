---

date: 2023-02-07 00:00:00-0700
categories: blog
author: Steve Springett
author_image: /assets/images/people/leader_springett.png
layout: blogpost
title: Vulnerability and Exploitability Transparency - VDR & VEX
excerpt_separator: <!--more-->

---

I've been meaning to write this article for about six months, and honestly, should have done it sooner. But let's get on
with it. With the rise of SBOM and software transparency, there is an equal push to be transparent about the vulnerabilities
and their exploitability in the software we create and consume. These are all good things. In this article, I'll be 
discussing two very different approaches, Vulnerability Disclosure Report (VDR) and Vulnerability Exploitability eXchange (VEX).


<!--more-->

While comparing and contrasting the approaches is useful, this article also serves to educate. Over the past 18 months,
I've seen several security tools incorporate "VEX" capabilities, not realizing what they actually support is VDR.
Clearly defining what these approaches are, their purpose, and how they compete and complement each other, is required
to level-set expectations between supplier and consumer.

__TL;DR__ Both VDR and VEX provide value to software consumers. Organizations should evaluate both strategies and implement
an approach that meets the requirements of all parties in their supply chain.

### Neutrality Statement
OWASP is known for its exceptionally high vendor neutrality standards, and while VDR and VEX are not vendors, they 
are differing ideas, both of which have merit. Both VDR and VEX are supported in [OWASP CycloneDX](https://cyclonedx.org) 
and [OWASP Dependency-Track](https://dependencytrack.org). I will not be taking a position, but it should be noted that 
there are many people and organizations in the industry that have political capital invested in one approach or the other.

### VDR and VEX Support in OWASP Projects
Two of the OWASP projects that I work on support both VDR and VEX. The rate of adoption of these projects is quite
staggering, but it's also provided the team with a lot of feedback from the community. While we do not capture usage data, 
we do engage in hundreds of conversations with the community. As a result, our team likely has some unique perspectives
on the real-world usage of VDR and VEX.

<div class="article-table"></div>


| Year | Support                                                                 |
|------|-------------------------------------------------------------------------|
| 2015 | VDR support in Dependency-Track v1.0 (API only)                         |
| 2018 | VDR support with analysis decisions in Dependency-Track v3.0 (API only) |
| 2019 | VDR support in CycloneDX v1.1 (extension only)                          |
| 2021 | VDR and VEX support in CycloneDX v1.4                                   |
| 2022 | VDR and VEX support in Dependency-Track v4.4 using CycloneDX v1.4       |


### What is VDR?
VDRs are an attestation of all vulnerabilities affecting a product, or its dependencies, along with an analysis of the impact. VDRs may 
come from a software supplier or a third party. [NIST SP 800-161: Cybersecurity Supply Chain Risk Management Practices for Systems and Organizations](https://csrc.nist.gov/publications/detail/sp/800-161/rev-1/final) 
defines VDR as:

<div class="article-quote"></div>

> Enterprises, where applicable and appropriate, may consider providing customers with a Vulnerability Disclosure Report
> (VDR) to demonstrate proper and complete vulnerability assessments for components listed in SBOMs. The VDR should 
> include the analysis and findings describing the impact (or lack of impact) that the reported vulnerability has on a 
> component or product. The VDR should also contain information on plans to address the CVE. Enterprises should consider
> publishing the VDR within a secure portal available to customers and signing the VDR with a trusted, verifiable, private
> key that includes a timestamp indicating the date and time of the VDR signature and associated VDR.

In summary, a VDR should contain:
- All vulnerabilities affecting a product or its dependencies
- Analysis describing the impact (or lack thereof) that a reported vulnerability has on a product or dependency
- Plans to address the vulnerability
- Signing the VDR with a trusted, verifiable, private key that includes a timestamp indicating the date and time of the VDR signature

### What is VEX?
VEX is a negative security advisory intended to state all vulnerabilities a product is not affected by. VEX got its start
within the [NTIA Software Transparency](https://ntia.gov/SoftwareTransparency) initiative and is now being spearheaded by [CISA](https://www.cisa.gov/sbom).
VEXs may come from a software supplier or a third party. VEX also includes:

- Analysis describing the impact (or lack thereof) that any vulnerability has on a product, product family, or organization
- Plans to address the vulnerability
- Signing the VEX with a trusted, verifiable, private key that includes a timestamp indicating the date and time of the VEX signature

VEX defines a minimal set of analysis decisions including:

#### Status
- not_affected
- affected
- fixed
- under_investigation

#### Justification
- Component_not_present
- Vulnerable_code_not_present
- Vulnerable_code_not_in_execute_path
- Vulnerable_code_cannot_be_controlled_by_adversary
- Inline_mitigations_already_exist

Note: CycloneDX includes a superset of both statutes and justifications that can be leveraged for both VDR and VEX use cases.

### What's the Difference?
On the surface, VDR and VEX look very similar. Both refer to vulnerabilities, both include an analysis of the impact,
and both include plans to address the vulnerabilities. So what's the difference? 

<div class="article-table"></div>

|                         | VDR                                                                                                                                                                                   | VEX                                                                                                                                                                                                           |
|-------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| __Scope__               | Product or dependencies (components and services)                                                                                                                                     | Product, product family, or entire organization                                                                                                                                                               |
| __Expectation__             | Asserts all vulnerabilities affecting a product, component or service                                                                                                                 | Negative security advisory intended to state all vulnerabilities a product is not affected by                                                                                                                 |
| __Vulnerability types__     | Known and previously unknown vulnerabilities                                                                                                                                          | Known vulnerabilities                                                                                                                                                                                         |
| __Analysis decision__       | Describes the impact of the vulnerability (if any), vendor response, and expectations                                                                                                 | Describes the impact of the vulnerability (if any), vendor response, and expectations                                                                                                                         |
| __Publish lifecycle__       | &bull;&nbsp;Published alongside SBOM<br/>&bull;&nbsp;Continuously updated when new vulnerabilities <u>affecting the product</u> are discovered or when analysis decisions are updated | &bull;&nbsp;Published alongside SBOM (except CSAF)<br/>&bull;&nbsp;Continuously updated when new vulnerabilities are published or when analysis decisions are updated                                         | 
| __Agency support__          | [NIST SP 800-161](https://csrc.nist.gov/publications/detail/sp/800-161/rev-1/final) recommendation                                                                                    | CISA (pseudo specification)                                                                                                                                                                                   |
| __Limitations__             | Overarching statements (e.g. entire organization) are not permitted                                                                                                                   | Cannot describe vulnerabilities that do not already have an identifier (e.g. previously unknown vulnerabilities)                                                                                              |
| __Formats and standards__   | CycloneDX, SAG-PM VDR                                                                                                                                                                 | CycloneDX, CSAF, OpenVEX (in development)                                                                                                                                                                     |
| __Risk transparency__       | Communicates risk and modified severity (CVSS temporal and environmental metrics, OWASP risk rating, etc) as it relates to the product                                                | Does not communicate risk or modified severity                                                                                                                                                                |
| __Attestation support__     | VDR is an attestation that the vendor has checked product dependencies for vulnerabilities and has communicated them                                                                  | VEX is an attestation of what vulnerabilities do not affect a product, and optionally, the ones that do. VEX does not require a vendor to check product dependencies for vulnerabilities, or communicate them | 
| __Tool availability__       | Widespread                                                                                                                                                                            | Limited                                                                                                                                                                                                       |
| __Results__                 | Consumers have a clear understanding of the vulnerabilities affecting a product and the vulnerabilities that do not                                                                   | Consumers have a clear understanding of the vulnerabilities affecting a product and the vulnerabilities that do not                                                                                           |


### Operationalizing VDR
Organizations that wish to utilize VDR will have a simple path forward. SBOMs assert inventory. VDRs assert 
vulnerabilities. Therefore, for minimal viable vulnerability management use cases, no analysis is required by the consumer
as the vulnerability analysis has already been performed by the supplier or trusted third party. This simplistic approach
to transparency lends itself to simple, easy-to-create tools that support this use case.

When new vulnerabilities are discovered, the VDR should be automatically updated by the vendor, who will eventually investigate
the vulnerability to determine its impact on the product.

VDR does not require SBOM but can complement one if present.

### Operationalizing VEX
On the surface, VEX also seems simple. However, many real-world complexities need to be resolved for organizations to 
successfully operationalize VEX.

Like VDR, VEX also does not require SBOM but can complement one if present.

The following are four use cases intended to illustrate commonly occurring success and failure paths.

#### Use Case 1: VEX and CVE Known to Vendor
- Consumer wants to know if product is affected by CVE-xxxx-xxxx, to which the vendor needs to respond
  - If an otherwise vulnerable dependency was not exploitable to CVE-xxxx-xxxx
    - Vendor would have a prepared response. Perfect!

This is a common scenario that the Dependency-Track community sees regularly and is a testament that VEX works.

#### Use Case 2: VEX Without SBOM and CVE Unknown to Vendor
- Consumer wants to know if product is affected by CVE-xxxx-xxxx, to which the vendor needs to respond
  - If the vendor is unaware of what CVE-xxxx-xxxx is, because the vulnerable component is not used by the product
    - Vendor would not be able to respond without additional research
    - Vendor would be responsible for triaging vulnerabilities with no relation to the product

As VEX is a negative security advisory, the consumer expectations default to the vendor product being exploitable. 

__Solution #1__: As a predictive measure, the vendor may choose to create VEX statements for commonly asked vulnerabilities, 
such as Log4Shell ([CVE-2021-44228](https://nvd.nist.gov/vuln/detail/CVE-2021-44228)), even if the product does not use 
Log4J or is even written in Java. This will allow the vendor to respond to uninformed consumers without access to SBOM data. 

__Solution #2__: It is difficult to predict what vulnerabilities a consumer will inquire about, therefore, some 
vendors may choose to support all 200K+ vulnerabilities in the NVD. This introduces additional complexity given that the 
CISA VEX specification requires individual vulnerability ID's, statutes, and justifications (or impact statements) for every 
vulnerability. This would make the VEX document incredibly large and will require vendors to operate VEX generation 
engines capable of integrating inventory from all products across their portfolio to truthfully respond with 
`Component_not_present` justifications.

To help vendors negate these scenarios, a future version of Dependency-Track will likely include support for one or both
of the solutions mentioned.

#### Context for Use Case 3-4
We often talk about the "naming problem" in the software world, which refers to the fact that the same piece of software
can have several names throughout its lifecycle. Unfortunately, the naming problem exists with vulnerabilities
as well. Turns out that "Common" in Common Vulnerability Enumeration (CVE) isn't very "Common" after all. CVE is just another
identifier and the NVD is just one of many sources of vulnerability intelligence.

To understand the decline of the NVD for application security use cases, one should read [New Recommendations to Improve The NVD](/blog/2022/09/13/sbom-forum-recommends-improvements-to-nvd.html).
The lack of Package URL or native package manager coordinate support has given rise to numerous vulnerability databases
that fill a need. The same vulnerability may exist in multiple vulnerability databases and have different identifiers across them.  
To help combat the naming problem, the [Open Source Vulnerability Schema](https://ossf.github.io/osv-schema/) project 
includes support for vulnerability aliasing. This is used by [osv.dev](https://osv.dev/) and [GitHub Advisories](https://github.com/advisories). 
Based on numerous feedback from the Dependency-Track community, aliasing is often unused, implemented incorrectly 
(via the 'related' field rather than 'alias'), or contains erroneous mappings.

And finally, many commercial SCA vendors have dedicated research teams that discover vulnerable open-source components and
do not share that data with the NVD. Better intelligence is one of the competitive advantages offered.

With all the context out of the way, let's dive into use cases 3 and 4.

#### Use Case 3: VEX With SBOM and Different Commercial Sources of Vulnerability Intelligence
This use case is similar to use case #2, but has important differences. The consumer in this case is well-informed. They
have an SBOM and are analyzing it for known vulnerabilities. However, both the vendor and consumer rely on different
sources of vulnerability intelligence, possibly commercial sources, which adds complexity.

- Consumer wants to know if product is affected by SCA-A-xxxx-xxxx, to which the vendor needs to respond
  - If the vendor is unaware of what SCA-A--xxxx-xxxx is, because they use SCA-B as a source of vulnerability intelligence
    - VEX will not "turn the lights off", even if the vulnerability is the same between SCA vendors. The vulnerability has an identifier unique to each SCA vendor, thus triggering the naming problem.

Use of the NVD is not practical when components have a Package URL and not a CPE. The use of alternatives to the NVD is 
quite common in these scenarios. When analyzing SBOMs, consumers will identify vulnerabilities that are not listed 
in the NVD, but are still publicly known. If the supplier of the VEX is not using the same source of vulnerability 
intelligence as the consumer, there may be lingering vulnerabilities whose analysis will not get updated due to the mismatch 
of vulnerability identifiers, or differences in the breadth of vulnerability intelligence between SCA vendors.

This is a common issue the Dependency-Track community sees from the real-world use of VEX.


#### Use Case 4: VEX With SBOM and Different Public Sources of Vulnerability Intelligence
This use case is very similar to #3 above, but focuses on public sources of vulnerability intelligence, including 
[OSS Index](https://ossindex.sonatype.org/), [osv.dev](https://osv.dev/), and [GitHub Advisories](https://github.com/advisories).

Public sources are different in that many vulnerabilities are not hidden behind paywalls, and the security community has 
a vested interest in ensuring they are accurate. As stated earlier both osv.dev and GitHub Advisories utilize the
Open Source Vulnerability Schema, which supports both `related` and `aliases` fields. Based on feedback from the 
Dependency-Track community, the use of these two fields is not consistent and oftentimes is unused or contains erroneous 
mappings. This is a classic case of Garbage-in/Garbage-out.

However, this is a solvable problem, but will take investment and coordination among the security community.


### Have it Both Ways

The NIST guidance in SP 800-161, further reads:

<div class="article-quote"></div>

> Enterprises should also consider establishing a separate notification channel for customers in cases where vulnerabilities 
> arise that are not disclosed in the VDR.

This point is crucial, as it leaves the door open for disclosing vulnerabilities that are too sensitive to communicate 
via normal channels, as well as the possibility to notify consumers about vulnerabilities they are not impacted by (VEX).

NIST guidance recommends that vendors issue VDRs as a regular practice, thus asserting what vulnerabilities a product is 
potentially affected by. NIST guidance also allows for the inclusion of VEX and similar notification strategies. 

Could it be that a hybrid approach of supporting both VDR and VEX is the way forward? 
In the end, hopefully, pragmatism will be the clear winner.


<style>
    .article-table + table { 
        width: 100%;
        margin-bottom: 2rem;
        word-break: normal;
    }
    .article-quote + blockquote { 
        font-style: italic;
    }
</style>