---

date: 2023-01-10 00:00:00-0700
categories: blog
author: Steve Springett
author_image: /assets/images/people/leader_springett.png
layout: blogpost
title: Celebrating 10 Years of OWASP Dependency-Track
excerpt_separator: <!--more-->

---

This year, [OWASP Dependency-Track](https://owasp.org/dependencytrack) is celebrating its 10th anniversary. It has been 
an unexpectedly wild ride, but an extremely gratifying and rewarding experience knowing that the project has helped 
countless individuals, organizations, and governments.


<!--more-->

### Background
Dependency-Track was founded in 2013 with a simple mission; to track the inventory of hardware and software components 
and identify any associated risk inherited from using them. If this sounds like Software Composition Analysis (SCA), 
you're partially correct, except unlike SCA, Dependency-Track relied on analyzing Bill of Materials (BOM) to achieve its 
mission.

My employer at the time was selling server appliances that would typically be deployed into customer datacenters. I had
a requirement to track the hardware, firmware, operating system, OS packages, applications, and application libraries for
every revision of these server appliances we brought to market. That was the original use case Dependency-Track was 
designed to solve. I hired an intern and later brought him on full-time to design and build out the initial prototype.

### Fast Forward
By March 2018, Dependency-Track v3.0 was released. Later that year, the U.S. [National Telecommunications and Information 
Administration (NTIA)](https://ntia.gov/) would kick off a multistakeholder [software component transparency effort](https://ntia.gov/other-publication/ntia-software-component-transparency). 
The end result of the NTIA work was the creation of multiple whitepapers and Software Bill of Materials (SBOM) 
requirements outlined in U.S. [Executive Order 14028](https://www.whitehouse.gov/briefing-room/presidential-actions/2021/05/12/executive-order-on-improving-the-nations-cybersecurity/). 

Between the years of 2018 to the present, the adoption of Dependency-Track accelerated faster than I could have 
imagined. Before 2018, Dependency-Track likely had less than 10 organizations using it. Today, it has more than
10,000 organizations using it, in production, and is responsible for analyzing over 300M components every month, minimum.

Those are just the numbers we know about and have been graciously provided by [Sonatype](https://www.sonatype.com/), who 
has been an amazing partner in this journey with their support for [OSS Index](https://ossindex.sonatype.org/), a freely 
available source of vulnerability intelligence that Dependency-Track integrates with out-of-the-box.

### Reflection
What started out as a pet project, has turned into a solution that government agencies rely on, 
enterprises standardize on, and has matured into a project that is "Flagship", or strategically important to the OWASP
Foundation and its mission. It has even given rise to [OWASP CycloneDX](https://owasp.org/cyclonedx), a Bill of Materials 
(BOM) standard, purpose built for software transparency and cyber risk reduction.

Experiencing this type of growth, and having such a positive impact on the software supply chain has been an extremely 
rewarding experience that the team does not take for granted. While Dependency-Track has come a long way from its origins, 
there's still much work to do.

### Celebration
So, this year we're going to celebrate. The project is responsible for a lot of industry "firsts" which we'll discover
in the weeks to come. We're going to celebrate our wins, learn from the times we don't, and most importantly, 
continue to fight the good fight in helping identify and reduce risk for the global software community.

Cheers.
