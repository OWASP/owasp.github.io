---

date:   2021-06-30 09:00:00 -0700
categories: Projects
author: Cristian Folini
author_image: /assets/images/people/portrait_christian_folini_3.jpg
layout: blogpost
title: CVE-2021-35368 - CRS Request Body Bypass
excerpt_separator: <!--more-->

---

The OWASP ModSecurity Core Rule Set (CRS) is affected by a request body bypass that abuses trailing pathname information. A backend vulnerability can thus be exploited despite being protected with the CRS Web Application Firewall rule set when an application server accepts additional path info as part of the request URI. All known CRS installations that offer the predefined CRS rule exclusion packages are affected. This applies to end-of-life CRS versions 3.1.0, 3.1.1 as well as the currently supported versions 3.2.0 and 3.3.0. Integrators and users are advised to upgrade.

For details and links to the new releases, please visit:
- <https://coreruleset.org/20210630/cve-2021-35368-crs-request-body-bypass/>
