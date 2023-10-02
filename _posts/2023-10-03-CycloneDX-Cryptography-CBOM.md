---

date: 2023-10-03 00:09:00-0700
categories: blog
author: Basil Hess and Nicklas Koertge
author_image: /assets/images/people/Basil-Hess-and-Nicklas Koertge.jpg
layout: blogpost
title: OWASP CycloneDX - The Missing Standard For Describing Cryptography in Software
excerpt_separator: <!--more-->

---

The CycloneDX Cryptography Working Group felt that the lack of a standard for describing cryptographic assets such as algorithms, certificates, or keys was a good starting point for working with the CycloneDX community to develop such. As part of our day-to-day work, it is not only important to have a consistent standard for representing cryptographic information, but also to establish it as part of a large ecosystem. Documenting the data and services placed at risk by a compromised cryptographic system is an investment in faster, more effective vulnerability response in the future.

<!--more-->

Advances in quantum computing introduce the risk of previously-secure cryptography algorithms becoming compromised faster than ever before. In May of last year, the White House released a [National Security Memorandum](https://www.whitehouse.gov/briefing-room/statements-releases/2022/05/04/national-security-memorandum-on-promoting-united-states-leadership-in-quantum-computing-while-mitigating-risks-to-vulnerable-cryptographic-systems/) outlining the government's plan to secure critical systems against potential quantum threats. This memorandum contains two key takeaways for both agency and commercial software providers: document the potential impact of a breach, and have an alternative cryptography solution ready.

As cryptographic systems evolve from using classical primitives to quantum-safe primitives, there is expected to be more widespread use of cryptographic agility, or the ability to quickly switch between multiple crypto primitives. Cryptographic agility serves as a security measure or incident response mechanism when a system's cryptographic primitive is discovered to be vulnerable or no longer complies with policies and regulations.

As part of an agile crypto approach, an organization needs to understand what cryptography it is using, which implies a crypto inventory. An inventory is a record of the cryptography in use with its location (e.g., which application) and associated vulnerabilities and policy violations. We needed a good starting point to describe such an inventory. In addition, it should support the assessment of the risk posture to provide a starting point for mitigation.

## Building on the strong foundation of CycloneDX
We knew that we needed something that intuitively represents the software composition and is extendable with information about cryptography. To address this need, the CycloneDX Cryptography Working Group is excited to announce ongoing work on a new capability of the CycloneDX SBOM standard: Cryptography Bill of Materials (CBOM). This capability allows cryptographic assets to be described and combined with other components, unlocking the possibility of a cryptographic inventory within a CycloneDX SBOM.

The next step for CBOM is integration of this capability with the already established CycloneDX SBOM standard. Steve Springett, chair of the CycloneDX standard, has already proposed integration for version 1.6 of CycloneDX, following the team making the CBOM extension open-source.

## How CBOM helps to give peace of mind with your crypto
A standard is only impactful if it can serve and drive use cases. By integrating the CBOM concept into SBOM, we inherit the use cases covered by CycloneDX SBOM and aim to close the delta between the existing standard and cryptographic use cases. A central aspect is awareness of cryptographic risk, for which CBOM helps with several use cases.

### Identify quantum unsafe and weak cryptography
Cryptographic algorithms differ in their security levels, they may be considered strong or weak against attacks using classical or quantum computers. Most notably, public key algorithms like RSA, DH, ECDH, DSA or ECDSA are considered not quantum-safe. These algorithms occur in various components and may be hardcoded in applications, but are more commonly and preferably used via dedicated cryptographic libraries or services. Developers often don’t directly interact with cryptographic algorithms such as RSA or ECDH but use them via protocols like TLS 1.3 or IPsec, by using certificates, keys or other tokens. With upcoming crypto agility it becomes less common to put in stone (or software) the algorithms that will be used. Instead they are configured during deployment or negotiated in each network protocol session. CBOM is designed with these considerations in mind and to allow insight into the classical and quantum security level of cryptographic assets and their dependencies.

### Inventory cryptographic assets

The migration to quantum safe cryptography usually starts with building a prioritized inventory of cryptographic systems. This is a requirement of the [OMB M-23-02](https://www.whitehouse.gov/wp-content/uploads/2022/11/M-23-02-M-Memo-on-Migrating-to-Post-Quantum-Cryptography.pdf), where such a system is characterized as a [..”software or hardware implementation of one or more cryptographic algorithms that provide one or more of the following services: (1) creation and exchange of encryption keys; (2) encrypted connections; or (3) creation and validation of digital signatures.”] While [EO 14028](https://www.whitehouse.gov/briefing-room/presidential-actions/2021/05/12/executive-order-on-improving-the-nations-cybersecurity/) has highlighted the importance of SBOMs, we think that CBOM as an extension of CycloneDX SBOM is an important step to be able to inventory cryptographic systems in a standardized form.

### Assess cryptographic policies and advisories
A cryptographic inventory in machine readable form like CBOM brings benefits if one wants to check for compliance with cryptographic policies and advisories. An example of such an advisory is [CNSA 2.0](https://media.defense.gov/2022/Sep/07/2003071834/-1/-1/0/CSA_CNSA_2.0_ALGORITHMS_.PDF), which was announced by NSA in September of last year. CNSA 2.0 states, among other things, that National Security Systems (NSS) for firmware and software signing need to support and prefer CNSA 2.0 algorithms by 2025 and exclusively use them by 2030. The advised algorithms are the stateful hash-based signature schemes LMS and XMSS from [NIST SP 800-208](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-208.pdf). With a CBOM inventory that documents the use of LMS and XMSS by such systems, compliance with CNSA 2.0 can be assessed in an automated way.

### Identify expiring and long-term cryptographic material
A RSA certificate expiring in one week poses less cryptographic risk than the same certificate expiring in 20 years. Service downtime due to an expired certificate is another risk to be considered. Therefore, we argue that an inventory that captures the life cycle of cryptographic material as allowed by CBOM gives context to an inventory that is instrumental for managing cryptographic risk.

### Ensure cryptographic certifications
Higher cryptographic assurance is provided by certifications such as [FIPS 140-3](https://csrc.nist.gov/pubs/fips/140-3/final) (levels 1 to 4) or [Common Criteria](https://www.commoncriteriaportal.org/) (EAL1 to 7). To obtain these certifications, cryptographic modules need to undergo certification processes. For regulated environments such as FedRAMP, such certifications are important requirements. CBOM allows to capture the certification level of cryptographic assets so that this property can be easily identified.

### Is this the end?
We don’t think so. Everything documented about cryptography in a standardized form instead of proprietary pdfs can be a use case. How about specifying the parameters or test vectors of an algorithm in CBOM? Or a CBOM property that implements an algorithm in 140 characters?

There are endless opportunities to further build upon CBOM in new and innovative ways, and the working group is only getting started. Anyone who would like to contribute feedback or work on the integration is welcome to join the weekly community working group, which meets at 8:00am -9:00 Central (01:00pm - 02:00pm UTC) every Thursday.

Visit the [#workstream-cryptography-bom](https://cyclonedx.slack.com/archives/C05E2FLUTNH) Slack channel to participate ([invite](https://cyclonedx.org/slack/invite)).

<style>
    .homepage-blog img {
        max-width: 200px !important;
    }
</style>