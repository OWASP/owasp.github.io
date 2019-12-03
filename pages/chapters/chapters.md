---
title: Chapters
layout: col-sidebar
permalink: /chapters
side_side: true
tags: chapters
---

OWASP Local Chapters foster local discussions of application security around the world. Our Local Chapter Meetings are free and open to anyone to attend so both members and non-members are alway welcomed. Chapters have general information and leader contact info on this website while running local meeting RSVPs through [https://meetup.com/pro/owasp](https://meetup.com/pro/owasp).

{% assign regions = site.data.chapters | map: 'region' | sort: region | uniq %}
<ul>
    {% for region in regions %}
        <li><a href='#{{ region | remove: " " }}'>{{ region }}</a>
    {% endfor %}
</ul>


## Join a Local Chapter
Attending meetings anywhere in the world is FREE and OPEN to anyone, membership is NOT required to do so. We suggest that you locate your "home chapter" and simply sign up on the appropriate mailing list, watch for the next local meeting stop by to introduce yourself ask questions and collaborate.


## Chapters by Geographic Region

<div class='chapters-list'>
    {% assign regions = site.data.chapters | map: 'region' | uniq %}
    {% for region in regions %}
        <div class="region">
            <a name='{{ region | remove: " " }}'</a><h2>{{ region }}</h2>
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
