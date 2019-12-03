---
title: OWASP Local Chapters
layout: col-sidebar
permalink: /chapters
side_side: true
tags: chapters
---

<img src="/assets/images/content/bay_area.jpg" alt="Bay Area Chapter Meeting">

OWASP Local Chapters build community for application security professionals around the world. Our Local Chapter Meetings are **free and open** to anyone to attend so both members and non-members are always welcomed. Local meetings include:

- Training to improve your skills
- Talks relevant to your work
- Networking opportunities

Chapter pages on this site have general information and leader contact info. Local meeting RSVPs are handled through [https://meetup.com/pro/owasp](https://meetup.com/pro/owasp).

## Local Chapter Quick Find
{% assign regions = site.data.chapters | map: 'region' | sort: region | uniq %}
<ul>
    {% for region in regions %}
    <li><a href='#{{ region | remove: " " }}'>{{ region }}</a></li>
    {% endfor %}
</ul>

<a href="https://meetup.com/pro/owasp" target="_blank" rel="noopener"><button class="cta-button dark">Search using Map</button></a>


## Chapters by Geographic Region

<div class='chapters-list'>
    {% assign regions = site.data.chapters | map: 'region' | sort: region | uniq %}
    {% for region in regions %}
        <div class="region">
            <h4><a name="{{ region | remove: " " }}"></a>{{ region }}</h4>
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
