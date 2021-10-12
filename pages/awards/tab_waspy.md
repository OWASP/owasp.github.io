---

title: WASPY
displaytext: WASPY Awards
layout:
tab: true
order: 2
tags: awd

---

## WASPY Awards














<!-- Keep the items below to change this to a data-driven format using _data/awards.yml 
{% comment %}
{% assign awards = site.data.awards | where: 'category', 'WASPY' | sort: 'year' | reverse %}
{% assign previous = nil %}
{%for award in awards %}
{% if previous != award.year %}
{% assign previous = award.year %}
### {{award.year}}
{% endif %}
**{{ award.title }} Winner{% if award.winners.size > 1%}s{%endif%}:**
{% for winner in award.winners %}
* {{ winner.name }}{%if winner.title %} ({{winner.title}}){% endif %}
{%- if winner.info -%}<br>{{winner.info}}{%- endif -%}
{% endfor %}
{%endfor%}
{% endcomment %}
-->