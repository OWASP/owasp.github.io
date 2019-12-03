---
title: Chapters
layout: col-sidebar
permalink: /chapters
side_side: true
tags: chapters
---

OWASP Local Chapters helps to foster local discussion of application security around the world. Our Local Chapters are free and open to anyone to attend. You do not need to be a member or donor of OWASP to attend. Local Chapters have pages on this website and run local meeting RSVPs through [https://meetup.com/pro/owasp](https://meetup.com/pro/owasp).

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
<script type="text/javascript">
    $(function(){
        $('#projects-type').click(function(){
            $('#project-list-level').hide();
            $('#project-list-type').show();
            $('#projects-level').removeClass('active');
            $('#projects-type').addClass('active');
            $('#projects-level').addClass('inactive');
            $('#projects-type').removeClass('inactive');
        });
        $('#projects-level').click(function(){
            $('#project-list-type').hide();
            $('#project-list-level').show();
            $('#projects-type').removeClass('active');
            $('#projects-level').addClass('active');
             $('#projects-level').removeClass('inactive');
            $('#projects-type').addClass('inactive');
        });
    });
</script>
