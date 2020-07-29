---

title: Upcoming OWASP Chapter Events (next 2 weeks)
layout: col-sidebar
permalink: /chapters/events/

---

{% for chapter in site.data.chapter_events %}
{% assign chevents = chapter.events | sort: 'date' %} 
{% for event in chevents %}
{% capture edate %}{{ event.date | date: '%F' }}{% endcapture %}
{% capture nowt %}{{'now' | date: '%s' | plus: 1209600 | date: '%F'}}{% endcapture %}
{% if edate < nowt %}
---
### Chapter: {{ chapter.chapter }}
#### Event: {{ event.name }}
#### Date: {{ edate }}
#### Link: [{{ event.link }}]({{ event.link }})
<div>
<strong>Description</strong>: {{ event.description }}
</div>
{% endif %}
{% endfor %}
{% endfor %}