---
title: OWASP Local Chapters
layout: col-sidebar
permalink: /chapters/
site_side: true
tags: chapters
---

<!-- rebuild 1 -->

<img src="/assets/images/web/chaper-wide.jpg" alt="Bay Area Chapter Meeting">

OWASP Local Chapters build community for application security professionals around the world. Our Local Chapter Meetings are **free and open** to anyone to attend so both members and non-members are always welcomed. Local meetings include:

- Training to improve your skills
- Talks relevant to your work
- Networking opportunities

Chapter pages on this site have general information and leader contact info. Local meeting RSVPs are handled through [https://meetup.com/pro/owasp](https://meetup.com/pro/owasp).

## Local Chapters by Region
{% assign regions = site.data.chapters | map: 'region' | sort: region | uniq %}
<ul>
    {% for region in regions %}
    <li><a href='#{{ region | remove: " " }}'>{{ region }}</a></li>
    {% endfor %}
</ul>

<a href="https://meetup.com/pro/owasp" target="_blank" rel="noopener"><button class="cta-button grey">Search using Map</button></a>


## Chapter Listing

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
