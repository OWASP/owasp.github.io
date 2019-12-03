---
title: Chapters
layout: col-sidebar
permalink: /chapters
side_side: true
tags: chapters
---

<img src="/assets/images/content/bay_area.jpg" alt="Bay Area Chapter Meeting">

OWASP Local Chapters foster lively discussions on application security around the world. Our Local Chapter Meetings are free and open to anyone to attend so both members and non-members are always welcomed. Chapters have general information and leader contact info on this website while running local meeting RSVPs through [https://meetup.com/pro/owasp](https://meetup.com/pro/owasp).

## Local Chapter Quick Find
{% assign regions = site.data.chapters | map: 'region' | sort: region | uniq %}
<ul>
    {% for region in regions %}
        <li><a href='#{{ region | remove: " " }}'>{{ region }}</a>
    {% endfor %}
</ul>

## Chapters by Geographic Region

<div class='chapters-list'>
    {% assign regions = site.data.chapters | map: 'region' | uniq %}
    {% for region in regions %}
        <div class="region">
            <h2><a name="{{ region | remove: " " }}"></a>{{ region }}</h2>
            <ul>
            {% for chapter in site.data.chapters %}
                {% if chapter.region == region %} 
                    <li><a href='{{ chapter.url }}'>{{ chapter.name }}</a></li>
                {% endif %}
            {% endfor %}
            </ul>
        </div>
    {% endfor %}
</div>
