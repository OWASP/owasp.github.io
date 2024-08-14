---

title: Election Results
displaytext: Election Results
layout:
tab: true
order: 3
tags: election

---

## Election Results
{% assign awards = site.data.awards | where: 'category', 'election' | sort: 'year' | reverse %}
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
<br>
{% endfor %}
{%endfor%}
