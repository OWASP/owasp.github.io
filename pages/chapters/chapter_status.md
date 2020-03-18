---

title: Chapter Status
layout: col-generic
permalink: /chapters/status/

---

## New Chapters

## Recently Updated Chapters

## Needs Website Update
<ul>
{% for chapter in site.data.chapters %}
    {% if chapter.region contains 'Website Update' %} 
        <li><a href='{{ chapter.url }}'>{{ chapter.title }}</a></li>
    {% endif %}
{% endfor %}
</ul>
