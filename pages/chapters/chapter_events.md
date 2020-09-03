---

title: Upcoming OWASP Chapter Meetup Events (next 30 days)
layout: col-sidebar
permalink: /chapters/events/

---

<br>
{% assign events = site.data.chapter_events | sort: 'date' %}
{% assign prevdate = nil %}

<!-- Index list -->

## Quick List (Details below)
{% assign i = 0 %}
{% for event in events %}
  {% assign evdate = event.date | date: "%b %d" %}
  * [{{ event.name }}]({{ i }}_item) by {{ event.chapter }} Chapter on {{ evdate }}
  {% assign i = i | plus: 1 %}
{% endfor %}

<!-- Full list -->
{% assign i = 0 %}
{% for event in events %}
{% assign evdate = event.date | date: "%B %d, %Y" %}
{% if evdate <> prevdate %}
---
## {{ evdate }}
---
{% assign prevdate = evdate %}
{% endif %}
### Event: <a name="#{{ i }}_item)">{{ event.name }} </a>
#### Chapter: [{{ event.chapter }}](/{{ event.repo }}/)
#### Time: {{ event.time }} ({{ event.timezone }})
#### Link: [{{ event.link }}]({{ event.link }})
<div>
<strong>Description</strong>: {{ event.description }}
</div>
<br>
  {% assign i = i | plus: 1 %}
{% endfor %}
