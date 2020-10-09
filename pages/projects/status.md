---

title: Project Website Status
layout: col-sidebar
permalink: /projects/status/

---

Jump to 
* [New Projects](#new)
* [Recently Updated](#updated)
* [Needs Update](#needs_update)
* [Last Update](#last-update)

### Total OWASP Projects: {{ site.data.projects.size }}

----
<section id='new'></section>

### New Projects (created within last 60 days)
{% assign year = "today" | date: "%Y" %}
{% assign month = "today" | date: "%m" %}
{% assign year = year | plus: 0 %}
{% assign month = month | plus: 0 %}

<ul>
{% for project in site.data.projects %}
    {% assign cyear = project.created | date: "%Y" %}
    {% assign cmonth = project.created | date: "%m" %}
    {% assign cyear = cyear | plus: 0 %}
    {% assign cmonth = cmonth | plus: 0 %}
    {% assign testmonth = month | minus: cmonth %}
    {% assign testyear = year | minus: 1 %}
    {% if cyear == year and testmonth  < 2 %} 
        <li><a href='{{ project.url }}'>{{ project.created }}, {{ project.title }}</a></li>
    {% elsif month <= 2 and cyear == testyear and cmonth >= 11 %}
        <li><a href='{{ project.url }}'>{{ project.created }}, {{ project.title }}</a></li>
    {% endif %}
{% endfor %}
</ul>

----
<section id='updated'></section>

### Recently Updated Projects (updated page within last 60 days)
<ul>
{% assign projects = site.data.projects | sort: 'updated' | reverse %}
{% for project in projects %}
    {% assign cyear = project.created | date: "%Y" %}
    {% assign cmonth = project.created | date: "%m" %}
    {% assign cyear = cyear | plus: 0 %}
    {% assign cmonth = cmonth | plus: 0 %}
    {% assign cuyear = project.updated | date: "%Y" %}
    {% assign cumonth = project.updated | date: "%m" %}
    {% assign custr = project.updated | date: "%Y-%m-%d" %}
    {% assign cuyear = cuyear | plus: 0 %}
    {% assign cumonth = cumonth | plus: 0 %}
    {% assign testmonth = month | minus: cumonth %}
    {% assign testyear = cuyear | minus: 1 %}
    {% if cuyear == year and testmonth < 2 %}
       {% unless cyear == year and cmonth == month %}
            {% unless  cyear == testyear and cmonth >= 11 %}
                {% unless project.region contains 'Website Update' %}
                    <li><a href='{{ project.url }}'>{{ custr }}, {{ project.title }}</a></li>
                {% endunless %}
            {% endunless %}
       {% endunless %}
    {% elsif cumonth <= 2 and cuyear == testyear and cumonth >= 11  %}
        {% unless cyear == year and cmonth == month %}
            {% unless  cyear == testyear and cmonth >= 11 %}
                {% unless project.region contains 'Website Update' %}
                    <li><a href='{{ project.url }}'>{{ custr }}, {{ project.title }}</a></li>
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
{% for project in site.data.projects %}
    {% if project.region contains 'Website Update' %} 
        <li><a href='{{ project.url }}'>{{ project.title }}</a></li>
    {% endif %}
{% endfor %}
</ul>

---
<section id='last-update'></section>

### All Projects and Most Recent Website Update
<ul>
{% assign projects = site.data.projects | sort: 'updated' | reverse %}
{% for project in projects %}
    {% assign custr = project.updated | date: "%Y-%m-%d" %}
      <li><a href='{{ project.url }}'>{{ custr }}, {{ project.title }}</a></li>
{% endfor %}
</ul>

---
Jump to 
* [New Projects](#new)
* [Recently Updated](#updated)
* [Needs Update](#needs_update)
* [Last Update](#last-update)
