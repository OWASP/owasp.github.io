---

title: Chapter Status
layout: col-generic
permalink: /chapters/status/

---

----
### New Chapters (created within last 60 days)
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
    {% if (cyear == year and month - cumonth < 2) or (cyear == year -1 and cmonth == 12) %} 
        <li><a href='{{ chapter.url }}'>{{ chapter.title }}</a></li>
    {% endif %}
{% endfor %}
</ul>

----
### Recently Updated Chapters (updated page within last 60 days)
<ul>
{% for chapter in site.data.chapters %}
    {% assign cyear = chapter.created | date: "%Y" %}
    {% assign cmonth = chapter.created | date: "%b" %}
    {% assign cyear = cyear | plus: 0 %}
    {% assign cmonth = cmonth | plus: 0 %}
    {% assign cuyear = chapter.updated | date: "%Y" %}
    {% assign cumonth = chapter.updated | date: "%b" %}
    {% assign cuyear = cuyear | plus: 0 %}
    {% assign cumonth = cumonth | plus: 0 %}
    {% if (cuyear == year and month - cumonth < 2) or (cuyear == year -1 and cumonth == 12) %}
       {% unless (cyear == year and cmonth == month) or (cyear == year -1 and cmonth == 12) %}
           {% unless chapter.region contains 'Website Update' %}
            <li><a href='{{ chapter.url }}'>{{ chapter.title }}</a></li>
           {% endunless %}
       {% endunless %}
    {% endif %}
{% endfor %}
</ul>

----
### Needs Website Update (has not been updated to remove default info)
<ul>
{% for chapter in site.data.chapters %}
    {% if chapter.region contains 'Website Update' %} 
        <li><a href='{{ chapter.url }}'>{{ chapter.title }}</a></li>
    {% endif %}
{% endfor %}
</ul>
