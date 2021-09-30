---

layout: col-sidebar
title: Corporate Membership
permalink: /supporters/list
site_side: true
tags: corp-membership

---

## Corporate Members, Sponsors & Supporters

_Disclaimer:_ The following information is not an endorsement for any particular entity and reflects the messaging of the supporter only.


{% assign supporters = site.data.corp_members | sort: 'name' %}

<h2>Diamond Corporate Event Sponsors</h2>
<ul style='list-style-type:none;     padding-inline-start: 0px;'>

{% assign level = site.data.sponsor_levels | where: 'level', -1 | first %}
{% for supporter in supporters %}
    {% if supporter.sponsor %}
        {% assign level = site.data.sponsor_levels | where: 'level', supporter.sponsor | first %}
    {% endif %}

    {% assign membertype = site.data.sponsor_levels | where: 'level', 4 | first %}
    {% if supporter.member and supporter.membertype %}
        {% assign membertype = site.data.sponsor_levels | where: 'level', supporter.membertype | first %}
    {% endif %}

    {% if level.level == 1 %}
        {% assign wstr = '300px' %}
        {% assign hstr = 'auto' %}
        {% if supporter.vertical == true %} {% assign wstr = 'auto' %}{% assign hstr = '75px' %}{% endif %}
        <li>
        <div>
        <a href = '{{ supporter.url }}' rel='noopener sponsored'><img src='{{ supporter.image }}' width='{{ wstr }}' height='{{ hstr }}'></a>
        <span style='float:right;'> 
        {% if supporter.member %}<img src='{{ membertype.memberimage }}' width='65px'>{% endif %}<img src ='{{ level.image }}' width="65px"> 
        </span>
        </div>
        <br>
        <p>
        {{ supporter.description }}
        {% assign supporterCount = supporterCount | plus:1 %}
        </p>
        </li>
        <hr>
    {% endif %}
{% endfor %}

<h2>Platinum Corporate Members and Sponsors</h2>

<ul style='list-style-type:none;     padding-inline-start: 0px;'>
{% assign level = site.data.sponsor_levels | where: 'level', -1 | first %}
{% for supporter in supporters %}
    {% if supporter.sponsor %}
        {% assign level = site.data.sponsor_levels | where: 'level', supporter.sponsor | first %}
    {% endif %}

    {% assign membertype = site.data.sponsor_levels | where: 'level', -1 | first %}
    {% if supporter.member %}
        {% if supporter.membertype %}
            {% assign membertype = site.data.sponsor_levels | where: 'level', supporter.membertype | first %}
        {% else %}
            {% assign membertype = site.data.sponsor_levels | where: 'level', 4 | first %}
        {% endif %}
    {% endif %}

    {% if level.level >= 0 and level.level < 2 %}
        {% assign supporter.sponsor = false %}
        {% assign level = site.data.sponsor_levels | where: 'level', -1 | first %}
        {% assign supporter.member = false %}
        {% assign membertype = site.data.sponsor_levels | where: 'level', -1 | first %}
    {% endif %}

    {% if membertype.level >= 0 and membertype.level < 2 %}
        {% assign supporter.sponsor = false %}
        {% assign level = site.data.sponsor_levels | where: 'level', -1 | first %}
        {% assign supporter.member = false %}
        {% assign membertype = site.data.sponsor_levels | where: 'level', -1 | first %}
    {% endif %}

    {% if membertype.level == 2 or level.level == 2 %}
        {% assign wstr = '250px' %}
        {% assign hstr = 'auto' %}
        {% if supporter.vertical == true %} {% assign wstr = 'auto' %}{% assign hstr = '75px' %}{% endif %}
        <li>
        <div>
        <a href = '{{ supporter.url }}' rel='noopener sponsored'><img src='{{ supporter.image }}' width='{{ wstr }}' height='{{ hstr }}'></a>
        <span style='float:right;'> 
        {% if supporter.member %}<img src='{{ membertype.memberimage }}' width='65px'>{% endif %}<img src ='{{ level.image }}' width="65px"> 
        </span>
        </div>
        <br>
        <p>
        {{ supporter.description }}
        </p>
        </li>
        <hr>
    {% endif %}
{% endfor %}

<h2>Gold Corporate Members and Sponsors</h2>

<ul style='list-style-type:none;     padding-inline-start: 0px;'>
{% assign level = site.data.sponsor_levels | where: 'level', -1 | first %}
{% for supporter in supporters %}
    {% if supporter.sponsor %}
        {% assign level = site.data.sponsor_levels | where: 'level', supporter.sponsor | first %}
    {% endif %}

    {% assign membertype = site.data.sponsor_levels | where: 'level', -1 | first %}
    {% if supporter.member %}
        {% if supporter.membertype %}
            {% assign membertype = site.data.sponsor_levels | where: 'level', supporter.membertype | first %}
        {% else %}
            {% assign membertype = site.data.sponsor_levels | where: 'level', 4 | first %}
        {% endif %}
    {% endif %}

    {% if level.level >= 0 and level.level < 3 %}
        {% assign supporter.sponsor = false %}
        {% assign level = site.data.sponsor_levels | where: 'level', -1 | first %}
        {% assign supporter.member = false %}
        {% assign membertype = site.data.sponsor_levels | where: 'level', -1 | first %}
    {% endif %}

    {% if membertype.level >= 0 and membertype.level < 3 %}
        {% assign supporter.sponsor = false %}
        {% assign level = site.data.sponsor_levels | where: 'level', -1 | first %}
        {% assign supporter.member = false %}
        {% assign membertype = site.data.sponsor_levels | where: 'level', -1 | first %}
    {% endif %}

    {% if membertype.level == 3 or level.level == 3 %}
        {% assign wstr = '180px' %}
        {% assign hstr = 'auto' %}
        {% if supporter.vertical == true %} {% assign wstr = 'auto' %}{% assign hstr = '75px' %}{% endif %}
        <li>
        <div>
        <a href = '{{ supporter.url }}' rel='noopener sponsored'><img src='{{ supporter.image }}' width='{{ wstr }}' height='{{ hstr }}'></a>
        <span style='float:right;'> 
        {% if supporter.member %}<img src='{{ membertype.memberimage }}' width='65px'>{% endif %}<img src ='{{ level.image }}' width="65px"> 
        </span>
        </div>
        <br>
        <p>
        {{ supporter.description }}
        </p>
        </li>
        <hr>
    {% endif %}
{% endfor %}

<h2>Silver Corporate Members and Sponsors</h2>

<ul style='list-style-type:none;     padding-inline-start: 0px;'>
{% assign level = site.data.sponsor_levels | where: 'level', -1 | first %}
{% for supporter in supporters %}
    {% if supporter.sponsor %}
        {% assign level = site.data.sponsor_levels | where: 'level', supporter.sponsor | first %}
    {% endif %}

    {% assign membertype = site.data.sponsor_levels | where: 'level', -1 | first %}
    {% if supporter.member %}
        {% if supporter.membertype %}
            {% assign membertype = site.data.sponsor_levels | where: 'level', supporter.membertype | first %}
        {% else %}
            {% assign membertype = site.data.sponsor_levels | where: 'level', 4 | first %}
        {% endif %}
    {% endif %}

    {% if level.level >= 0 and level.level < 4 %}
        {% assign supporter.sponsor = false %}
        {% assign level = site.data.sponsor_levels | where: 'level', -1 | first %}
        {% assign supporter.member = false %}
        {% assign membertype = site.data.sponsor_levels | where: 'level', -1 | first %}
    {% endif %}

    {% if membertype.level >= 0 and membertype.level < 4 %}
        {% assign supporter.sponsor = false %}
        {% assign level = site.data.sponsor_levels | where: 'level', -1 | first %}
        {% assign supporter.member = false %}
        {% assign membertype = site.data.sponsor_levels | where: 'level', -1 | first %}
    {% endif %}

    {% if membertype.level == 4 or level.level == 4 %}
        {% assign wstr = '150px' %}
        {% assign hstr = 'auto' %}
        {% if supporter.vertical == true %} {% assign wstr = 'auto' %}{% assign hstr = '75px' %}{% endif %}
        <li>
        <div>
        <a href = '{{ supporter.url }}' rel='noopener sponsored'><img src='{{ supporter.image }}' width='{{ wstr }}' height='{{ hstr }}'></a>
        <span style='float:right;'> 
        {% if supporter.member %}<img src='{{ membertype.memberimage }}' width='65px'>{% endif %}<img src ='{{ level.image }}' width="65px"> 
        </span>
        </div>
        <br>
        <p>
        {{ supporter.description }}
        </p>
        </li>
        {% if not forloop.last %}<hr>{% endif %}
    {% endif %}
{% endfor %}

</ul>
