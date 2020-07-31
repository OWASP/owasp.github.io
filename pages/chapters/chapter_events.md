---

title: Upcoming OWASP Chapter Meetup Events (next 30 days)
layout: col-sidebar
permalink: /chapters/events/

---

<br>
{% assign events = site.data.chapter_events | sort: 'date' %}
{% for event in events %}
---
### Chapter: [{{ event.chapter }}](/{{ event.repo }}/)
{% assign chevents = chapter.events | sort: 'date' %} 
{% for event in chevents %}
{% assign evdate = event.date | date: "%B %d, %Y" %}
---
#### Event: {{ event.name }}
#### Date: {{ evdate }}
#### Time: {{ event.time }} ({{ event.timezone }})
#### Link: [{{ event.link }}]({{ event.link }})
<div>
<strong>Description</strong>: {{ event.description }}
</div>
<br>
{% endfor %}
{% endfor %}
