---

layout: col-generic
title: Corporate Sponsorship

---

## Corporate Sponsorship
Organizations looking to support the mission of OWASP while also interested in exhibiting at conferences like our Global AppSec events, should consider Corporate Sponsorship. These packages offer the best value and include:
- Event Exhibtion space - up to five events per year
- Discounted conference and training passes
- Listing in rotation as Corporate Supporter site-wide on owasp.org
- Public acknowledgment on various other channels

## Packages

### Diamond - Premier package
- Exhibition space (typically 8'x6') at all Global AppSec events and up to THREE Regional Events
- Three complimentary Full Conference passes to exhibiting events
- Ten single-day Training Passes
- Ten-day on-site training
- Full Conference 50% off discounted passes
- Price: $120,000

### Platinum
- Exhibition space (typically 8'x6') at all Global AppSec events and up to TWO Regional Events
- Three complimentary Full Conference passes to exhibiting events
- Ten single-day Training Passes
- Five-day on-site training
- Full Conference 50% off discounted passes
- Price: $80,000

### Gold
- Exhibition space (typically 8'x6') at up to TWO Global AppSec events and ONE Regional Events
- Three complimentary Full Conference passes to exhibiting events
- Ten single-day Training Passes
- Full Conference 20% off discounted passes
- Price: $45,000

### Silver
- Exhibition space (typically 8'x6') at ONE Global AppSec events and ONE Regional Events
- Three complimentary Full Conference passes to exhibiting events
- Two single-day Training Passes
- Full Conference 20% off discounted passes
- Price: $25,000

All Sponsorship Packages include:
- Online and on-premise logo and recognition
- Lead scanner at exhibiting events

## Event Sponsorship
If you're looking to simply exhibit an one of our conferences, you can also support the Foundation with an Event Sponsorship.  Pricing and benefits vary by event. Please click on the links below to learn more about those particular offerings.

### Global AppSec Events
<ul>
{% assign eventlist = site.data.events | where_exp: "event", "event.type contains 'global'" | sort: 'start-date' | limit: 100 %}
{% for event in eventlist %}
<li><a href='{{ event.url }}' target='_blank'>{{ event.name }}</a>, {{ event.dates }}. {% if event.optional-text %}{{ event.optional-text }}{% endif %}</li>
{% endfor %}
</ul>

### Regional Events
<ul>
{% assign eventlist = site.data.events | where_exp: "event", "event.type contains 'local'" | sort: 'start-date' | limit: 100 %}
{% for event in eventlist %}
<li><a href='{{ event.url }}' target='_blank'>{{ event.name }}</a>, {{ event.dates }}. {% if event.optional-text %}{{ event.optional-text }}{% endif %}</li>
{% endfor %}
</ul>

If you're ready to learn more, please [Contact Us](https://owasporg.atlassian.net/servicedesk/customer/portal/7/group/18/create/72){:rel="noopener sponsored" target="_blank"}.
