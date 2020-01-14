---

layout: col-generic
title: Corporate Supporters
permalink: /supporters/

---

![Attendees at a Global AppSec Conference](/assets/images/web/global-conference.png)

The Open Web Application Security Project (OWASP) is a nonprofit foundation that works to improve the security of software. Our programming includes:

- Community-led open source software projects
- Over 275 local chapters worldwide
- Tens of thousands of members
- Industry-leading educational and training conferences

<p class="callout-mono right">Corporate support accelerates our impact. Become a member or sponsor today.</p>

We are an open community dedicated to enabling organizations to conceive, develop, acquire, operate, and maintain applications that can be trusted. All of our projects ,tools, documents, forums, and chapters are free and open to anyone interested in improving application security. For nearly two decades corporations, foundations, developers, and volunteers have supported the OWASP Foundation and its work. 

## Supporting the Foundation
There are many ways to participate and support the mission of OWASP.
- Employees can participate in our [Projects](/projects) and [Local Chapters](/chapters)
- Become a Corporate Member
- Sponsor the Foundation and our Events
- Make a [charitable gift](/donate) to the Foundation to support our ongoing work.

## Corporate Membership
Choosing to be a Corporate Member of the OWASP Foundation demonstrates your organization’s commitment to information security. Annual Corporate Membership pricing begins at $5,000 and is dependent on yearly revenue.  Organizations up to $50 million the fee is $5,000. For those between $50 million and $100 million the annual fee is $15,000. And for companies with yearly revenue more than $100 million the Corporate Membership Fee is $25,000.  All memberships include:
- Listing in rotation as Corporate Supporter site-wide on owasp.org
- Up to $2,500 of your Fee can be applied to Corporate Sponsorship
- Public acknowledgment on various other channels

To learn more please [Contact Us](https://owasporg.atlassian.net/servicedesk/customer/portal/7/group/18/create/72){:rel="noopener sponsored" target="_blank"} today!

## Corporate Sponsorship
Organizations looking to support the mission of OWASP while also interested in exhibiting at conferences like our Global AppSec events, should consider Corporate Sponsorship. These packages offer the best value and include:
- Event Exhibtion space - up to five events per year
- Discounted conference and training passes
- Listing in rotation as Corporate Supporter site-wide on owasp.org
- Public acknowledgment on various other channels

Visit [Corporate Sponsorship](/pages/corporate-sponsorships) to learn more about these packages. And if you're ready, please [Contact Us](https://owasporg.atlassian.net/servicedesk/customer/portal/7/group/18/create/72){:rel="noopener sponsored" target="_blank"} today!

---
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
