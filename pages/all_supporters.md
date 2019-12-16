---

layout: col-generic
title: Corporate Supporters
permalink: /supporters

---

---
_Disclaimer:_ The following information is not an endorsement for any particular entity and reflects the messaging of the supporter only.

---

{% assign supporters = site.data.corp_members %}

<ul style='list-style-type:none;     padding-inline-start: 0px;'>

{% for supporter in supporters %}
{% if supporter.sponsor %}
{% assign level = site.data.sponsor_levels | where: 'level', supporter.sponsor | first %}
{% else %}
{% assign level = '' %}
{% endif %}
{% assign wstr = '200px' %}
{% assign hstr = 'auto' %}
{% if supporter.vertical == true %} {% assign wstr = 'auto' %}{% assign hstr = '75px' %}{% endif %}
<li>
<div>
<a href = '{{ supporter.url }}' rel='noopener sponsored'><img src='{{ supporter.image }}' width='{{ wstr }}' height='{{ hstr }}'></a>
<span style='float:right;'> 
{% if supporter.member %}<img src='/assets/images/member.png' width='65px'>{% endif %}<img src ='{{ level.image }}' width="65px"> 
</span>
</div>
<br>
<p>
{{ supporter.description }}
</p>
</li>
<hr>
{% endfor %}

</ul>