---

layout: col-generic
title: Corporate Supporters

---

![Attendees at a Global AppSec Conference](/assets/images/web/global-conference.png)

The Open Web Application Security Project (OWASP) is a nonprofit foundation that works to improve the security of software. Our programming includes:

- Community-led open source software projects
- Over 200+ local chapters worldwide
- Tens of thousands of members
- Industry-leading educational and training conferences

<p class="callout-mono right">Corporate support accelerates our impact. Become a member or sponsor today.</p>

We are an open community dedicated to enabling organizations to conceive, develop, acquire, operate, and maintain applications that can be trusted. All of our projects, tools, documents, forums, and chapters are free and open to anyone interested in improving application security. For nearly two decades corporations, foundations, developers, and volunteers have supported the OWASP Foundation and its work. 

## Supporting the Foundation

There are many ways to participate and support the mission of OWASP.

- Employees can participate in our [Projects](/projects) and [Local Chapters](/chapters)
- Become a Corporate Member
- Sponsor the Foundation and our Events
- Make a [charitable gift](/donate) to the Foundation to support our ongoing work.

## Corporate Membership

Becoming a Corporate Member of the OWASP Foundation demonstrates your organization’s commitment to information security. We have Corporate Membership plans from $800 on up, including regional discounts, startup discounts, and various tiers with increasing benefits.

All memberships include:

- Listing in rotation as Corporate Supporter site-wide on owasp.org
- Discounts on [Event Sponsorship](https://owasp.org/corporate-sponsorships) packages
- Public acknowledgment on social media and other channels
- Vote in the Global Board of Directors election

There are many additional benefits based upon the tier you choose.

[You can learn more about our Corporate Membership packages](https://owasp.org/supporters/) or please [Contact Us](https://owasporg.atlassian.net/servicedesk/customer/portal/7/group/18/create/72){:rel="noopener sponsored" target="_blank"} today!

## Event Sponsorship

Organizations wishing to make contact with developers and appsec professionals, whilst also supporting OWASP's mission, should consider exhibiting at OWASP [Global AppSec or AppSec Days events](https://owasp.org/events/).

All our [Event Sponsorship packages can be found here](https://owasp.org/corporate-sponsorships) or please [Contact Us](https://owasporg.atlassian.net/servicedesk/customer/portal/7/group/18/create/72){:rel="noopener sponsored" target="_blank"} today to learn more!

## Corporate Members, Sponsors & Supporters

_Disclaimer:_ The following information is not an endorsement for any particular entity and reflects the messaging of the supporter only.


{% assign supporters = site.data.corp_members %}

<ul style='list-style-type:none;     padding-inline-start: 0px;'>

{% for supporter in supporters %}
{% if supporter.sponsor %}
{% assign level = site.data.sponsor_levels | where: 'level', supporter.sponsor | first %}
{% else %}
{% assign level = '' %}
{% endif %}
{% assign wstr = '200px' %}
{% assign hstr = 'auto' %}
{% if supporter.vertical == true %} {% assign wstr = 'auto' %}{% assign hstr = '75px' %}{% endif %}
<li>
<div>
<a href = '{{ supporter.url }}' rel='noopener sponsored'><img src='{{ supporter.image }}' width='{{ wstr }}' height='{{ hstr }}'></a>
<span style='float:right;'> 
{% if supporter.member %}<img src='/assets/images/member.png' width='65px'>{% endif %}<img src ='{{ level.image }}' width="65px"> 
</span>
</div>
<br>
<p>
{{ supporter.description }}
</p>
</li>
<hr>
{% endfor %}

</ul>
