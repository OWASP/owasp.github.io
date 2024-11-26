---

date: 2024-11-26 00:00:00-0700
categories: blog
author: Olle Johansson and Benji Visser
author_image: /assets/images/people/Olle-Johansson-and-Benji-Visser.jpg
layout: blogpost
title: Lifecycle events are part of the secure supply chain
excerpt_separator: <!--more-->

---
_A new OWASP project - Common Lifecycle Enumeration - aims to standardize encodings of product lifecycle events, such as end-of-life, end-of-support and others. The specification will become an ECMA International standard when ready. Read more about this exciting new OWASP project!_

<!--more-->

Digital products, both hardware and software have a lifecycle that mirrors human life - they are born, grow and develop, and eventually come to an end,  just like ourselves. However, there are many more changes in a product’s lifecycle that need to be captured, both for commercial products and open source software. The end-of-life state will affect many users of a product in various ways and needs to be communicated in a way that supports a high degree of automation.

When building a product today, we combine components from a range of upstream vendors and open source projects - a motherboard, operating system, sensors, software libraries and tools. The bill-of-materials (BOM) is a necessary tool to manage both hardware and software during the lifetime of the product. The BOM, when combined with lifecycle events, provides a foundation for automating and proactively managing each product’s lifecycle.

## Regulators require product lifecycle management

New regulations, like the recently adopted EU Cyber Resilience Act, enforces a lifecycle management process where manufacturers are obliged to maintain security through the product’s entire lifecycle, from purchasing to decommissioning. This means manufacturers must ensure that the product and all components are secure, kept up-to-date, and free of exploitable vulnerabilities.

The [OWASP CycloneDX](https://cyclonedx.org/) bill-of-materials standard can cover many aspects of a product, both software and hardware. But one thing that’s been missing is just the lifecycle events, like end-of-support, end-of-life and end-of-sales. For Open Source projects there are similar events covering “LTS release support”, “security fixes only”, “stable” and other variants.

## Monitoring the life state of a product or component is essential

A manufacturer needs to be assured that components from upstream vendors and projects are supported, otherwise the manufacturer assumes full responsibility.

A customer, through their  IT organization, also wants to be able to plan their inventory and capture this  information from all vendors. Products without any support need to be phased out in a controlled and planned way with as few surprises as possible.

## Lifecycle management requires a high degree of automation

This exchange of information across the supply chain needs to be both enumerated in a standard format and automatically exchanged. Rest assured that OWASP is working on all fronts here.

The [OWASP Common Lifecycle Enumeration (CLE) project](/cle/) is actively working on a standard for capturing these events. This will be part of the effort to standardize OWASP standards in [ECMA TC54](https://tc54.org/). The summer of 2024 CycloneDX became an ECMA standard and more is on the way. A new working group, ECMA TC54 TG3, was formed in October 2024 to lead the standardization alongside working groups for the Package URL (PURL) and the Transparency Exchange API.

## How OWASP CLE fits into other work

The CLE syntax will be adopted by the [OWASP Transparency Exchange API (TEA)](https://github.com/CycloneDX/transparency-exchange-api)  working group (also known as “Project Koala”) that creates a standardized set of APIs for publishing and consuming software and hardware transparency artifacts like SBOM, HBOM, VEX/CSAF vulnerability information, IN-Toto attestations, SCITT statements and much more. With TEA the interaction between customers and vendors will be highly automated. A standard API leads not only to efficient workflows, but also keeps costs for integration under control. Many vendors of platforms have shown interest in integration TEA into their systems, including [OWASP Dependency Track](https://dependencytrack.org/), a leading open source platform for software transparency, license compliance and vulnerability management.

If you're interested, all are welcome to join the work in the OWASP common lifecycle enumeration project!

[https://owasp.org/www-project-common-lifecycle-enumeration/](https://owasp.org/www-project-common-lifecycle-enumeration/)

<div style="display: flex; flex-wrap: wrap;">
    <div style="flex: 1; min-width: 50%; padding-top: 3rem;">
      <strong>Benji Visser</strong><br>Leader of OWASP CLE
    </div>
    <div style="flex: 1; min-width: 50%; padding-top: 3rem;">
      <strong>Olle E. Johansson</strong><br>Leader of OWASP CycloneDX project Koala
    </div>
  </div>

<style>
    .homepage-blog img {
        width: 150px !important;
        max-width: 200px !important;
        border:none;
    }
</style>
