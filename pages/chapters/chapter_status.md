---

title: Chapter Status
layout: col-sidebar
permalink: /chapters/status/

---

Jump to 
* [New Chapters](#new)
* [Recently Updated](#updated)
* [Needs Update](#needs_update)
* [Last Update](#last-update)
* [Inactive](#inactive)


### Total OWASP Chapters: {{ site.data.chapters.size }}

----
<section id='new'></section>

### New Chapters (created within last 60 days)
{% assign year = "today" | date: "%Y" %}
{% assign month = "today" | date: "%m" %}
{% assign year = year | plus: 0 %}
{% assign month = month | plus: 0 %}
<ul>
{% for chapter in site.data.chapters %}
    {% assign cyear = chapter.created | date: "%Y" %}
    {% assign cmonth = chapter.created | date: "%m" %}
    {% assign cyear = cyear | plus: 0 %}
    {% assign cmonth = cmonth | plus: 0 %}
    {% assign testmonth = month | minus: cmonth %}
    {% assign testyear = year | minus: 1 %}
    {% if cyear == year and testmonth  < 2 %} 
        <li><a href='{{ chapter.url }}'>{{ chapter.created }}, {{ chapter.title }}</a></li>
    {% elsif month <= 2 and cyear == testyear and cmonth >= 11 %}
        <li><a href='{{ chapter.url }}'>{{ chapter.created }}, {{ chapter.title }}</a></li>
    {% endif %}
{% endfor %}
</ul>

----
<section id='updated'></section>

### Recently Updated Chapters (updated page within last 60 days)
<ul>
{% assign chapters = site.data.chapters | sort: 'updated' | reverse %}
{% for chapter in chapters %}
    {% assign cyear = chapter.created | date: "%Y" %}
    {% assign cmonth = chapter.created | date: "%m" %}
    {% assign cyear = cyear | plus: 0 %}
    {% assign cmonth = cmonth | plus: 0 %}
    {% assign cuyear = chapter.updated | date: "%Y" %}
    {% assign cumonth = chapter.updated | date: "%m" %}
    {% assign custr = chapter.updated | date: "%Y-%m-%d" %}
    {% assign cuyear = cuyear | plus: 0 %}
    {% assign cumonth = cumonth | plus: 0 %}
    {% assign testmonth = month | minus: cumonth %}
    {% assign testyear = cuyear | minus: 1 %}
    {% if cuyear == year and testmonth < 2 %}
       {% unless cyear == year and cmonth == month %}
            {% unless  cyear == testyear and cmonth >= 11 %}
                {% unless chapter.region contains 'Website Update' %}
                    <li><a href='{{ chapter.url }}'>{{ custr }}, {{ chapter.title }}</a></li>
                {% endunless %}
            {% endunless %}
       {% endunless %}
    {% elsif cumonth <= 2 and  cuyear == testyear and cumonth >= 11  %}
        {% unless cyear == year and cmonth == month %}
            {% unless  cyear == testyear and cmonth >= 11 %}
                {% unless chapter.region contains 'Website Update' %}
                    <li><a href='{{ chapter.url }}'>{{ custr }}, {{ chapter.title }}</a></li>
                {% endunless %}
            {% endunless %}
        {% endunless %}
    {% endif %}
{% endfor %}
</ul>

----
<section id='needs_update'></section>

### Needs Website Update (has not been updated to remove default info)
<ul>
{% for chapter in site.data.chapters %}
    {% if chapter.build != 'no pages' and chapter.region contains 'Website Update' %} 
        <li><a href='{{ chapter.url }}'>{{ chapter.title }}</a></li>
    {% endif %}
{% endfor %}
</ul>

----
<section id='inactive'></section>

### Inactive Chapters 
<ul>
{% assign chapters = site.data.chapters | sort: 'title' %}
{% for chapter in chapters %}
  {% if chapter.build == 'no pages' %}
    <li>{{ chapter.title }}</li>
  {% endif %}
{% endfor %}
</ul>

---
<section id='last-update'></section>

### All Chapters and Most Recent Update
<ul>
{% assign chapters = site.data.chapters | sort: 'meetings' | reverse %}
{% for chapter in chapters %}
    {% assign custr = chapter.updated | date: "%Y-%m-%d" %}
    {% assign status_color = 'black' %}
    {% assign meeting_color = 'black' %}
    {% if chapter.build == 'errored' %}
       {% assign status_color = 'red' %}
    {% endif %}
    {% if chapter.meetings < 3 %}
       {% assign meeting_color = 'red' %}
    {% endif %}
      <li><div style='display:block;'><a href='{{ chapter.url }}'>{{ chapter.title }}</a></div>
      <div style='float:left;padding-right:24px;'>Last Updated: {{ custr }}</div>
      <div style='display:block;'><span style='color:{{status_color}};'>Build Status: {{ chapter.build }} </span></div>
      <div style='display:block;'><span style='color:{{meeting_color}};'>Meetings last 365 days: {{chapter.meetings}}</span></div></li>
{% endfor %}
</ul>

---
Jump to 
* [New Chapters](#new)
* [Recently Updated](#updated)
* [Needs Update](#needs_update)
* [Last Update](#last-update)
* [Inactive](#inactive)
