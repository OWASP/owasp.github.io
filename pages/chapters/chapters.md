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
{% assign regions = site.data.supported_regions %}
<ul>
    {% for region in regions %}
    <li><a href='#{{ region.region | remove: " " }}'>{{ region.region }}</a></li>
    {% endfor %}
</ul>

<a href="https://meetup.com/pro/owasp" target="_blank" rel="noopener"><button class="cta-button grey">Search using Map</button></a>


## Chapter Listing

<div class='chapters-list'>
    {% assign regions = site.data.supported_regions %}
    {% for region in regions %}
        {% assign rcount = 0 %}
        <div class="region">
            <h4><a name="{{ region.region | remove: " " }}"></a>{{ region.region }}</h4>
            <ul>
            {% for chapter in site.data.chapters %}
                {% if chapter.region == region.region and chapter.build != 'no pages'%}
                {% assign rcount = rcount | plus: 1 %}
                    <li><a href='{{ chapter.url }}'>{{ chapter.title }}</a></li>
                {% endif %}
            {% endfor %}
            </ul>
            Total: {{rcount}}
        </div>
    {% endfor %}
</div>


## Chapters in Unsupported Regions
{% for chapter in site.data.chapters %}
    {% assign in_region = false %}
    {% for region in site.data.supported_regions %}
        {% if chapter.region == region.region and chapter.build %}
            {% assign in_region = true %}
        {% endif %}
    {% endfor %}
    {%- if in_region == false -%}
        - [{{chapter.title}}]({{chapter.url}}) in {{ chapter.region }}
    {% endif %}
{% endfor %}
