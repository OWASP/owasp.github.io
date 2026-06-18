---

date: 2026-06-18 00:00:00-0700
categories: blog
author: Andrew van der Stock
author_image: /assets/images/corp-member-logo/Aikido.png
layout: blogpost
title: Aikido and OWASP bring agentic Code Audit to the global AppSec community
excerpt_separator: <!--more-->

---

Aikido Security and OWASP launch a new individual member benefit:  pentester-grade code audits, powered by AI reasoning.

<!--more-->
---

**Gent, Belgium [June 18th, 2026]** Aikido Security, the all-in-one developer security platform, today announced a new individual member benefit in partnership with the Open Worldwide Application Security Project (OWASP). The program gives every OWASP individual member **200 free Aikido credits** to run Code Audit; a new class of static code analysis that uses reasoning models to find the kinds of vulnerabilities that have, until now, required a human pentester to dig up.

OWASP is an online community that produces freely available articles, methodologies, documentation, tools, and technologies in the fields of IoT, system software and application security.

AI Code Audit reads source directly and reasons about intent across a codebase the way a senior security engineer would. Rather than matching syntactic patterns, the agents follow references across files and modules to surface the issues that need an attacker’s perspective: insecure direct object references (IDORs), broken access controls, multi-step exploit chains, business logic flaws, authentication bypasses, and privilege escalation. Reviews aren’t limited to web applications. The agents work across mainstream languages, configuration, and infrastructure-as-code, and they treat the whole repository as in scope, including monorepos with multiple services or packages, mobile apps, smart contracts, and desktop applications.

In the joint collaboration with OWASP, Aikido has made AI Code Audit credits available to all OWASP individual members for 6 months starting today (June 18th, 2026). Members redeem their credits in Aikido, connect a repository, and start an audit. No live environment, staging URL, or auth setup required.

---

### Where AI Code Audit Sits Between SAST and Pentest

Static scanners flag patterns: a tainted parameter, a risky API call, a missing check. They’re fast and deterministic, and they catch a well-understood class of vulnerability: SQL injection, XSS, command injection, hardcoded secrets, insecure deserialization. But pattern matching is structurally blind to the vulnerabilities that require business and code context to identify, like an IDOR across the order, payment, and user services, or a rate-limit bypass that depends on multi-step state.

AI Code Audit is a different engine for that different class of vulnerability. Think of it as a light AI pentest, run against your source code rather than a live target. It complements SAST rather than replacing it: SAST runs on every commit and catches what rules can describe; AI Code Audit goes deeper where rules fall short, catching IDORs, privilege escalation, cross-service logic flaws, and authentication bypasses in multi-step flows.

Because AI Code Audit reads source directly, there’s no crawl phase, no traffic replay, and no live environment to point at. End users can run it on whatever codebase they care about, including projects without a stable staging or QA target. For teams that also want runtime validation, AI Code Audit pairs naturally with Aikido Pentest, which confirms exploitability against the running application.

---

### What Aikido and OWASP Are Saying

>“We built AI Code Audit to give developers the kind of deep, contextual code reasoning that used to require an experienced human pentester. OWASP members are exactly the people we want putting it through its paces: they push the field forward and they hold us to a high bar. Making this benefit available to every individual member is our way of saying thanks for the work the community does,” said Willem Delbare, CEO and co-founder of Aikido Security.

>“The OWASP mission is to make the best application security resources available to the community building the world’s software. We’re pleased to work with Aikido Security to put a new class of reasoning-based code audit in the hands of our individual members, helping them find logic-layer issues that traditional tooling misses,” said **Andrew van der Stock, Executive Director of OWASP**.

>“IDORs, broken access control, and business logic flaws are some of the hardest issues to catch in code, and they show up in nearly every codebase we look at,” said Maarten De Schuymer, Head of Product at Aikido Security. “Giving OWASP members credits to run AI Code Audit on the projects they care about is a small way to help the community ship safer software.”

---

### How OWASP Members Can Claim the Benefit

OWASP individual members can claim their credits and run their first AI Code Audit at [https://www.aikido.dev/code/code-audit](https://www.aikido.dev/code/code-audit). The program runs for 6 months starting today (June 18th, 2026). Cost per audit depends on the size and complexity of the repositories selected; the exact credit total is shown in Aikido before the audit begins.

---

### About OWASP
The OWASP Foundation is a nonprofit organization that works to improve the security of software. Through community-led open source software projects, over 260 local chapters worldwide, tens of thousands of members, and leading educational and training conferences, the OWASP Foundation is the source for developers and technologists to secure the web. For nearly two decades, corporations, foundations, developers, and volunteers have supported the OWASP Foundation and its work. To learn more or to become a member, visit [owasp.org](owasp.org).

---

