---

title: Distinguished
displaytext: Distinguished Lifetime
layout: null
tab: true
order: 1
tags: awd

---
## Distinguished Lifetime Membership Awards

{% assign awards = site.data.awards | where: 'category', 'Distinguished Lifetime' | sort: 'year' | reverse %}
{% assign previous = nil %}
{%for award in awards %}
{% if previous != award.year %}
{% assign previous = award.year %}
<hr>
<h2>{{award.year}}</h2>
{%endif%}
<br>
<hr>
* <h3>{{award.title}}</h3>
{% for winner in award.winners %}
    * ![{{winner.name}}]({{winner.image}}){:width="80px"}&nbsp;&nbsp;&nbsp;{{winner.name}}
{%- if winner.info -%}
     <br>{{winner.info}}
{%- endif -%}
<br><br>
{% endfor %}
{%endfor%}