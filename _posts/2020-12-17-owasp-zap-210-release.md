---

date: 2020-12-17
author: Andrew van der Stock
author_image: /assets/images/people/staff_andrew.jpg
layout: blogpost
title: "ZAP 10th Birthday Release!!!"
excerpt_separator: <!--more-->

---

Guest post from Simon Bennetts, better known as [@psiion](https://twitter.com/psiinon), and the entire [Zap team](https://twitter.com/zaproxy). ^ ajv

## A Quick Introduction to ZAP

In 2009 I was a Java developer and a pentest on one of my services found vulnerabilities that I’d never even heard of. I decided that I needed to learn more about web application security in order to become a better developer.

I quickly discovered OWASP and started going through the wealth of material available, but I knew that I learn best by doing things so I started downloading and playing around with open source security tools. At that time I was also looking for an open source project to contribute to, so this seemed the ideal opportunity to combine those two things. Unfortunately there were not any actively maintained open source web security tools back then, so I took the plunge, forked Paros Proxy (which had been taken closed source) and set out to create the community-led open source project that I wanted to join. Since then ZAP has gone from strength to strength and we now have a core team and hundreds of [contributors](https://www.zaproxy.org/docs/desktop/credits/).

<!--more-->

ZAP has become one of OWASP’s most popular projects and is, we believe, the most frequently used web application [scanner in the world](https://www.zaproxy.org/blog/2020-04-02-is-zap-the-worlds-most-popular-web-scanner/).

As you may know ZAP has a plugin architecture which allows us to add new add-ons and update existing add-ons without a new ZAP release. However, there is a core set of functionality that we can only update with a full release.

## The ZAP 2.10.0 Release

ZAP 2.10.0 has just been released and is now available to download via [https://www.zaproxy.org/download/](https://www.zaproxy.org/download/)

Some of the more significant enhancements include:

- **Custom Pages**. [Custom Pages](https://www.zaproxy.org/docs/desktop/start/features/custompages/) can be defined on a per context basis - these allow ZAP to identify various non-standard error handling conditions such as custom error pages and handle them more effectively.
- **Authentication Polling**. The concept of [Authentication Verification Strategies](https://www.zaproxy.org/docs/desktop/start/features/authstrategies/) has been introduced which allows ZAP to handle a wider range of authentication mechanisms including the option to poll a specific page (or endpoint) for the authentication status of a user.
- **Site Tree Control**. Scripts and add-ons now have full access to how nodes are represented in the [Sites Tree](https://www.zaproxy.org/docs/desktop/start/features/sitestree/). Both [Input Vector Scripts](https://github.com/zaproxy/community-scripts/tree/master/variant) and add-ons which include implementations of the [Variant](https://static.javadoc.io/org.zaproxy/zap/2.10.0/org/parosproxy/paros/core/scanner/Variant.html) class can change both the tree structure and display names used for new nodes. For more details see the [Site Tree Modifiers Blog post](https://www.zaproxy.org/blog/2020-09-22-sites-tree-modifiers/).
- **Dynamic Look and Feel including Dark Mode**. The Desktop UI includes a new set of open source Look and Feel's c/o [FlatLaf](https://github.com/JFormDesigner/FlatLaf) including 2 Dark Mode options.You can also dynamically switch the Look and Feel via a button on the [Top Level Toolbar](https://www.zaproxy.org/docs/desktop/ui/tltoolbar/). For more details of the dark mode see the [Dark Mode in the Weekly Release Blog post](https://www.zaproxy.org/blog/2020-03-04-dark-mode-in-the-weekly-release/).
- **Authentication Headers via Env Vars**. A new set of environmental variables are available which allow you to easily add an authentication header to all of the requests that are proxied through ZAP or initiated by the ZAP tools, including the spiders and active scanner. These are documented on the Authentication page.
- **SOCKS Proxy Configuration**. It is now possible to dynamically configure the outgoing SOCKS proxy in the Options' Connection screen. By default the SOCKS proxy configuration applies to all connections made by ZAP.
- **Cached Scripts**. The following script types are now cached between invocations reducing the time it takes to reuse them:

  - Active Rules
  - HTTP Sender
  - Input Vectors, when used for the Sites tree
  - Passive Rules
  - Proxy
  - New Add-Ons
  
The following add-ons are included by default in this release for the first time:

- [Advanced Encode / Decode / Hash dialog](https://www.zaproxy.org/docs/desktop/addons/encode-decode-hash/) - this replaces the old core encode/decode/hash dialog.
- [DOM XSS Scan Rule](https://www.zaproxy.org/docs/desktop/addons/dom-xss-active-scan-rule/) - an Active Scan rule for detecting DOM XSS vulnerabilities.
- [Form Handler](https://www.zaproxy.org/docs/desktop/addons/form-handler/) - allows for the custom configuration of values used in forms based on field names.
- [GraalVM JavaScript](https://www.zaproxy.org/docs/desktop/addons/graalvm-javascript/) - included as Java 15+ no longer includes the Oracle Nashorn JavaScript engine.
- [GraphQL Support](https://www.zaproxy.org/docs/desktop/addons/graphql-support/) - allows you to import and active scan GraphQL definitions.
- [Retire.js](https://www.zaproxy.org/docs/desktop/addons/retire.js/) - a Passive Scan rule which implements checks provided by [Retire.js](https://retirejs.github.io/retire.js/) in order to identify vulnerable or out-dated JavaScript packages.
- [SOAP Support](https://www.zaproxy.org/docs/desktop/addons/soap-support/) - allows you to import and active scan WSDL files containing SOAP endpoints.

For the full set of changes, including changes to the Docker images, the updated add-ons, smaller enhancements and bug fixes see the [Release Notes](https://www.zaproxy.org/docs/desktop/releases/2.10.0/).

A big thank you to everyone who has contributed to this release or has supported the ZAP project in any way!
