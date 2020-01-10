---

layout: col-generic
title: OWASP Global & Regional Events
permalink: /events

---
![Attendees at a Global AppSec Conference](/assets/images/web/events-header.png)

Ever wanted to network and learn along with other AppSec professionals? We host nearly a dozen events each year varying in format to week long trainings and conferences, to single day programs. OWASP events are a great way to:

- Improve you career skills
- Build your professional network
- Learn about new trends in the industry

While some of our events have corporate sponsors, the content is vendor neutral, and speakers are carefully selected ensuring a good return on your investment of time and money. Often times are larger events also host Expositions, Capture the Flags, and Career Fairs. Often members get a discount on conference passes.

Skip to <a href="#regionalevents">Regional Events</a> or <a href="#globalpartnerevents">Global Partner Events</a>

## Global Events

Our premier events with up to three days of training followed by a two day conference with keynotes and multiple tracks. A global team plans the agenda, selects the speakers, and hosts the event.

{% assign eventlist = site.data.events | where_exp: "event", "event.type contains 'global'" | sort: 'start-date' | limit: 100 %}
{% for event in eventlist %}
<h4>{{ event.name }}</h4>
<ul>
<li>{{ event.dates }}</li>
{% if event.optional-text %}<li>{{ event.optional-text }}</li>{% endif %}
<li><a href='{{ event.url }}/?utm_source=owasp-web&utm_medium=event-page&utm_campaign=none' target='_blank'>{{ event.url }}</a></li>
</ul>
{% endfor %}

<a name="regionalevents">
## Regional Events

Ranging from single day to week long events, local OWASP volunteers organize and host conferences around the world. 

{% assign eventlist = site.data.events | where_exp: "event", "event.type contains 'local'" | sort: 'start-date' | limit: 100 %}
{% for event in eventlist %}
<h4>{{ event.name }}</h4>
<ul>
<li>{{ event.dates }}</li>
{% if event.optional-text %}<li>{{ event.optional-text }}</li>{% endif %}
<li><a href='{{ event.url }}?utm_source=owasp-web&utm_medium=event-page&utm_campaign=none' target='_blank'>{{ event.url }}</a></li>
</ul>
{% endfor %}

<a name="globalpartnerevents">
## Global Partner Events

Throughout the year, the OWASP Foundation partners with major AppSec conferences to offer discounted tickets and other benefits for OWASP members. If you would like to establish a global partnership with us please contact [Partnership Marketing](mailto:lisa.jones@owasp.com?subject=Partnership%20Marketing) for more information.

#### BlackHat Asia 2020
- March 31 - April 3, 2020
- Marina Bay Sands / Singapore
- $ 200.00 discount code available - members email marketing@owasp.org
- [Registration Site](https://www.blackhat.com/asia-20/)
