---

date: 2023-03-01 00:00:00-0700
categories: blog
author: Steve Springett
author_image: /assets/images/people/leader_springett.png
layout: blogpost
title: OWASP Foundation Announces CycloneDX Project Momentum with Contribution from IBM to Advance Software Supply Chain Security
excerpt_separator: <!--more-->

---

[The OWASP Foundation](https://owasp.org/) (Open Worldwide Application Security Project) and [IBM](https://www.ibm.com/) 
today announced IBM’s contribution of two open source projects, [SBOM Utility](https://github.com/CycloneDX/sbom-utility) 
and [License Scanner](https://github.com/CycloneDX/license-scanner), to [CycloneDX](https://cyclonedx.org/), a flagship 
OWASP project and a leading Bill of Materials (BOM) standard. These projects promote the validation, content analysis and
accuracy of software license information included within BOMs in support of increasing trust across open hardware and 
software supply chains.

<!--more-->

IBM developed SBOM Utility and License Scanner and will contribute the open source technologies to OWASP to help developers
enhance their quality of data on the front end and help validate SBOMs to assess risk. IBM actively contributes and
maintains a leadership role in industry-leading and up-and-coming open source communities, helping developers and business
partners in the IBM Ecosystem manage their open source strategies.

“There is still a need for awareness, tooling and guidance to help create software with more security features,” said 
Jamie Thomas, General Manager, Systems Strategy and Development, IBM. “IBM has a long history of contributing to a wide 
variety of open source communities such as the OWASP Foundation. We believe these contributions can help developers assess
risk and create more secured applications that can build consumers trust.”

## SBOM Utility
This utility is designed to be an API platform used primarily to validate CycloneDX or SPDX format BOMs against their 
published schemas. Furthermore, it can help validate derivative, “custom” schemas created by corporations, industries 
groups or organizations that will want stricter BOM data requirements to be enforced. Its ability to perform queries 
against CycloneDX BOM contents with regular expressions (regex) and generate custom reports can provide immediate value 
to organizations that consume BOMs. For example, it can evaluate and report on component software, service and data 
license information to assist organizations in risk evaluation against configurable usage policies.

The tool's ability to validate and analyze encompasses all CycloneDX BOM types including Hardware (HBOM), 
Software-as-a-Service (SaaSBOM) and others, each having different data requirements and levels of maturity, which reflects
the need for increasingly domain-specific validation of BOM contents. Specifically, this utility intends to support the 
work of the OWASP Software Component Verification Standard (SCVS), which is defining a BOM Maturity Model (BMM) to help 
in identifying and reducing risk in the software supply chain. Additionally, it can process documents that include the 
Vulnerability Disclosure Report (VDR), and Vulnerability Exploitability eXchange (VEX) data formats, as defined by 
CycloneDX, to aid in risk assessment.

The tool can operate standalone or as part of Continuous Integration and Delivery (CI/CD) tool chains producing JSON,
Text, CSV or Markdown enabling simplified downstream consumption.

## License Scanner
License Scanner is designed to scan files for licenses and legal terms. It can be used to help identify text matching 
licenses and license exceptions from the complete, published [SPDX License List](https://spdx.org/licenses/). License 
Scanner out-of-the-box matches against the 3.18 release of the SPDX licenses (a little less than 500) and license 
exceptions (40+) and comes with an option to import future versions of SPDX licenses. It can also be configured to 
identify additional legal terms, keywords, aliases, and non-SPDX licenses. As a library, License Scanner is designed to 
be integrated into existing BOM generation software or may be used by itself as a command-line utility.

License Scanner CLI offers functionalities to scan a single file or whole directories and returns the license IDs along 
with the copyrights. License-scanner CLI also provides an option to identify the blocks of text which match with a 
specified set of licenses and return the exact positions of such license matches.

Specifically, it scans the license text against the set of SPDX license templates and returns the CycloneDX LicenseChoice 
data incorporating three ways of expressing licenses: SPDX License ID, SPDX License Expression, and License name.

License Scanner was developed for integration into [IBM Cloud’s Continuous Delivery](https://www.ibm.com/cloud/continuous-delivery) 
Service’s DevOps toolchains and is also used as part of IBM’s legal clearance process for open-source and corporate 
software before approval for internal use.

Both tools are written in Go to take advantage of the language's built-in typing enforcement and memory safe features 
and its ability to be compiled for a wide range of target platforms and architectures and be compatible with cloud 
native platforms.

“OWASP thanks IBM for these contributions to the OWASP CycloneDX project. The validation against defined schemas is an 
important integrity control, and the ability to scan code to identify licenses is critical for some use cases. For many
mergers and acquisitions, being able to rapidly and accurately identify licenses present in code make or break deals. 
I am a huge fan of the Go language, and it heartens me that safer languages are being used for mission-critical work. 
I look forward to seeing how our community, developers and organizations will end up using these contributions,” said 
Andrew van Der Stock, Executive Director, OWASP.

### **About CycloneDX**

OWASP CycloneDX is a full-stack Bill of Materials (BOM) standard that provides advanced supply chain capabilities for 
cyber risk reduction. The CycloneDX project provides standards in XML, JSON, and Protocol Buffers, as well as a 
[large collection of official and community supported tools](https://cyclonedx.org/tool-center/) that create and 
interoperate with the standard. The project encourages community participation in the development of the standard and 
supporting tools. Visit [https://cyclonedx.org](https://cyclonedx.org/) for more information.

### **About the OWASP Foundation**

The Open Worldwide Application Security Project (OWASP) is a nonprofit organization that works to improve the security of
software. Through community-led open source software projects, over 260 local chapters worldwide, tens of thousands of
members, and leading educational and training conferences, the OWASP Foundation is the source for developers and
technologists to secure the web. For over two decades corporations, foundations, developers, and volunteers have
supported the OWASP Foundation and its work. To learn more or to become a member, visit [https://owasp.org](https://owasp.org).

OWASP and the Open Worldwide Application Security Project are trademarks of the OWASP Foundation.
