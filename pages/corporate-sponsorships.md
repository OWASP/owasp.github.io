---

layout: col-generic
title: Corporate Sponsorship

---

![Exhibitor at Global AppSec Amsterdam during sessions](/assets/images/web/exhibition.png)

Organizations looking to support the mission of OWASP while also interested in exhibiting at conferences like our Global AppSec events, should consider Corporate Sponsorship. These packages offer the best value and include:
- Event Exhibition space - up to five events per year
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
If you're looking to simply exhibit at one of our conferences, you can also support the Foundation with an Event Sponsorship.  Pricing and benefits vary by event. Please click on the links below to learn more about those particular offerings.



{% for category in site.data.events %}
<a name='{{category.category}}'>

<div style='height:45px;background:#f4f6fc;line-height:45px;padding-left:16px;'>
<h3>{{ category.category }} Events</h3>
</div>

{{ category.description }}
{% if category.events == nil or category.events.size < 1 %}
***No events upcoming.  Check back later.***
{% endif %}
{% for event in category.events %}
#### {{ event.name }}
<ul>
<li>{{ event.dates }}</li>
{% if event.optional-text %}<li>{{ event.optional-text }}</li>{% endif %}
<li><a href='{{ event.url }}/?utm_source=owasp-web&utm_medium=event-page&utm_campaign=none' target='_blank'>{{ event.url }}</a></li>
</ul>
{% endfor %}
{% endfor %}

<div style='height:45px;background:#f4f6fc;'></div>
If you're ready to learn more, please [Contact Us](https://owasporg.atlassian.net/servicedesk/customer/portal/7/group/18/create/72){:rel="noopener sponsored" target="_blank"}.

Please note certain restrictions may apply. Benefits are NOT transferable and expire following the end of the exhibiting conferences.
