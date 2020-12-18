---

layout: col-generic
title: OWASP Global & Regional Events
permalink: /events/

---
![Attendees at a Global AppSec Conference](/assets/images/web/events-header.png)

Ever wanted to network and learn along with other AppSec professionals? We host nearly a dozen events each year varying in format to week long trainings and conferences, to single day programs. OWASP events are a great way to:

- Improve your career skills
- Build your professional network
- Learn about new trends in the industry

While some of our events have corporate sponsors, the content is vendor neutral, and speakers are carefully selected ensuring a good return on your investment of time and money. Often times are larger events also host Expositions, Capture the Flags, and Career Fairs. Often members get a discount on conference passes.

Skip to {% for category in site.data.events %}<a href="#{{category.category}}"><strong>{{category.category}} Events</strong></a> {%unless forloop.last %},{%endunless%} {% endfor %}

{% for category in site.data.events %}
<a name='{{category.category}}'>
## {{ category.category }} Events

{{ category.description }}
{% if category.events == nil or category.events.size < 1 %}
***No events upcoming.  Check back later.***
{% endif %}
{% for event in category.events %}
{% if event.url %}
<h4><a href='{{event.url}}/?utm_source=owasp-web&utm_medium=event-page&utm_campaign=none' target='_blank'>{{event.name}}</a></h4>
{% else %}
<h4>{{ event.name }}</h4>
{% endif %}
<ul>
<li>{{ event.dates }}</li>
{% if event.optional-text %}<li>{{ event.optional-text }}</li>{% endif %}
</ul>
{% endfor %}
{% endfor %}
