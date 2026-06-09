---

date: 2026-06-09 00:00:00-0700
categories: blog
author: 
author_image: 
layout: blogpost
title: OWASP Dependency-Track 5.0 Is Now Generally Available
excerpt_separator: <!--more-->

---

### OWASP Dependency-Track 5.0 Is Now Generally Available

The largest redesign in the project's history brings horizontal scaling, fault tolerance, and software supply chain integrity verification to the widely used open source platform

<!--more-->
---

[Wilmington, DE], June 3, 2026. OWASP Dependency-Track, the open source platform that organizations use to identify and reduce risk in the software supply chain, today announced the general availability of version 5.0. Developed under the codename Hyades, v5 is the most extensive redesign since the platform's inception. It rebuilds how Dependency-Track scales, survives failure, and reasons about risk, while keeping the workflows teams already rely on.

Version 4 ran as a single API server that held its work queue in memory and its search index on local disk. That shape served smaller deployments well, but it limited any team that needed high availability, predictable resource usage, or clean recovery after a crash. Version 5 targets those limits directly. The platform now scales out, keeps working when individual instances fail, and standardizes on a single mature database engine. Smaller deployments gain the same guarantees with no added complexity.

Those guarantees already hold up in the field. Early adopters running the v5 alphas have ingested upwards of 20,000 SBOMs per hour, and some organizations now operate single v5 instances holding more than 250,000 SBOMs representing tens of millions of software components. Throughput and portfolio sizes at that level put Dependency-Track firmly in enterprise territory.

---

### 🛍️ Highlights of Dependency-Track 5.0

- Horizontal scaling and active/active high availability. Stateless API server instances coordinate through PostgreSQL alone, with no message broker and no peer to peer networking, so a cluster can span availability zones and scale up or down without reconfiguration.

- Processing that survives crashes. An embedded durable execution engine resumes bill of materials processing, vulnerability analysis, and notification delivery from the exact step they reached, and retries failed steps automatically with backoff instead of waiting for someone to trigger them again.

- Software supply chain integrity verification. Dependency-Track now flags components whose published hashes do not match what the upstream package registry served, catching typosquatting and registry side tampering, a class of attack that v4 left to tools further down the pipeline.

- Smarter, expression based policies. A new policy engine built on Common Expression Language (CEL) powers component policies, vulnerability policies that can automatically audit or suppress findings before they reach analysts, and notification filters that can match on any field of an event, such as firing only at or above a chosen severity.

- - One database, fewer failure modes. v5 standardizes on PostgreSQL and moves search, caching, and metrics into the database. The local search index disappears, along with the index corruption and disk space failures that came with it, and metrics become a proper time series with bounded retention.

Built for operations. A dedicated management endpoint exposes Prometheus metrics and Kubernetes style liveness and readiness probes on their own port, integration secrets are centralized behind a pluggable provider for easier rotation and audit, and pluggable file storage supports shared volumes or S3 compatible object storage.

- Governance and data lifecycle. Portfolio access control graduates out of beta with bounded overhead at scale, and configurable retention keeps inactive project versions and time series metrics from growing without bound.

---

### What it means for security leaders

For security leaders, v5 turns Dependency-Track into infrastructure they can depend on at enterprise scale. The strategic value is less about any single feature than about what a platform at this scale makes possible.

Regulation is turning software inventory from good practice into legal obligation. Under the EU Cyber Resilience Act, manufacturers of products with digital elements must produce and maintain a machine readable SBOM, with core obligations phasing in through December 2027 and vulnerability reporting duties arriving sooner. Satisfying that across a real product portfolio means keeping a complete and continuously updated inventory, not a periodic sample. v5 is built to hold exactly that, at the scale where compliance has to operate.

The same foundation reaches well beyond software. A platform that already tracks millions of components is the natural place to inventory everything else an organization ships and runs, including hardware, AI and machine learning models, and the cryptography embedded across its products.


> "Dependency-Track has always been about making software bill of materials analysis practical for everyone, and v5 is about making it dependable at any  scale, from a single team to enterprise portfolios of hundreds of thousands of projects," said Steve Springett, founder and project co-lead of OWASP  Dependency-Track. "We rebuilt the engine so the platform stays up, never silently loses work, and gives teams stronger guarantees about the integrity of what they ship, without losing the openness that made the project what it is."


The strategic premise underneath all of it is simple: an organization cannot assess, prioritize, or reduce risk in what it has not inventoried. By making a complete and current component inventory feasible at enterprise scale, v5 gives security and risk teams the foundation that every downstream assessment depends on, whether regulatory, vulnerability, license, cryptographic, or supply chain.


---

### What it means for existing v4 users

Existing Dependency-Track 4.x deployments continue to receive security and high severity fixes on the 4.14.x line for at least roughly six months after this release. v5 does not upgrade in place: it runs on its own PostgreSQL cluster and ingests v4 data through an offline, one time migrator, so teams should plan a maintenance window.

Operators should note the headline breaking changes. PostgreSQL is now the only supported database, replacing H2, MySQL, and Microsoft SQL Server. Notification payloads move to Protobuf, so existing templates need updating. The REST API enforces pagination by default and changes some response schemas. The bundled container image and the executable WAR are discontinued in favor of separate API server and frontend container images. Lucene based fuzzy vulnerability matching is removed. Full upgrade and migration guides, including a rehearsal procedure and a parallel run option, are available in the documentation.


>"This release was two years in the making, and not a line of it happened in isolation," said Niklas Düster, co-leader of OWASP Dependency-Track and lead architect of v5. "Countless individuals and organizations contributed code, infrastructure, funding, and feedback, and many ran the early builds in production so we could scale v5 against real workloads. We are deeply grateful to every one of them. Dependency-Track v5 is a community effort, and it shows."
---

### Availability
Dependency-Track 5.0 is available now as container images from Docker Hub and the GitHub Container Registry. Documentation, upgrade guides, and the v4 to v5 migration procedure are published at the project documentation site. Dependency-Track is free and open source under the OWASP Foundation.
---

### About OWASP Dependency-Track
OWASP Dependency-Track is an OWASP flagship project and an intelligent component analysis platform that helps organizations identify and reduce risk in the software supply chain. It consumes software bill of materials (SBOM) data, including the CycloneDX standard, continuously monitors components for newly disclosed vulnerabilities and policy violations, and integrates with the tools that security and development teams already use. Learn more at dependencytrack.org[dependencytrack.org](https://dependencytrack.org/).

---

