---

title: Chapter Status
layout: col-generic
permalink: /chapters/status/

---

----
### New Chapters
{% assign year = "today" | date: "%Y" %}
{% assign month = "today" | date: "%b" %}
{% assign year = year | plus: 0 %}
{% assign month = month | plus: 0 %}

<ul>
{% for chapter in site.data.chapters %}
    {% assign cyear = chapter.created | date: "%Y" %}
    {% assign cmonth = chapter.created | date: "%b" %}
    {% assign cyear = cyear | plus: 0 %}
    {% assign cmonth = cmonth | plus: 0 %}
    {% if cyear == year and cmonth == month %} 
        <li><a href='{{ chapter.url }}'>{{ chapter.title }}</a></li>
    {% endif %}
{% endfor %}
</ul>

----
### Recently Updated Chapters
<ul>
{% for chapter in site.data.chapters %}
    {% assign cuyear = chapter.updated | date: "%Y" %}
    {% assign cumonth = chapter.updated | date: "%b" %}
    {% assign cuyear = cuyear | plus: 0 %}
    {% assign cumonth = cumonth | plus: 0 %}
    {% if cuyear == year and cumonth == month %}
       {% unless chapter.region contains 'Website Update' %}
        <li><a href='{{ chapter.url }}'>{{ chapter.title }}</a></li>
       {% endunless %}
    {% endif %}
{% endfor %}
</ul>

----
### Needs Website Update
<ul>
{% for chapter in site.data.chapters %}
    {% if chapter.region contains 'Website Update' %} 
        <li><a href='{{ chapter.url }}'>{{ chapter.title }}</a></li>
    {% endif %}
{% endfor %}
</ul>
