---

title: Upcoming OWASP Chapter Events (next 30 days)
layout: col-sidebar
permalink: /chapters/events/

---

{% for chapter in site.data.chapter_events %}
---
### Chapter: [{{ chapter.chapter }}](/{{ chapter.repo }}/)
{% assign chevents = chapter.events | sort: 'date' %} 
{% for event in chevents %}
---
#### Event: {{ event.name }}
#### Date: {{ event.date }}
#### Time: {{ event.time }} ({{ event.timezone }})
#### Link: [{{ event.link }}]({{ event.link }})
<div>
<strong>Description</strong>: {{ event.description }}
</div>
{% endfor %}
{% endfor %}
