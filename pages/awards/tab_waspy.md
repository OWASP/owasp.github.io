---

title: WASPY
displaytext: WASPY Awards
layout:
tab: true
order: 2
tags: awd

---
## WASPY Awards
<section class="corporate">

{% assign awards = site.data.awards | where: 'category', 'WASPY' | sort: 'year' | reverse %}
{% assign previous = nil %}
{%for award in awards %}
{% if previous != award.year %}
{% assign previous = award.year %}
<hr>
<h3>{{award.year}}</h3>
{% endif %}
<h3>{{ award.title }}{% if award.winners.size > 1%}s{%endif%}</h3><br>
{% for winner in award.winners %}
<div class="member-container">
{% if winner.image %}<div class="member-img-container"><img src="{{winner.image}}" alt="{{winner.name}}" class="member-img"></div>{% endif %}<div class="member-caption"><strong>{{ winner.name }}</strong>{%if winner.title %}({{winner.title}}){% endif %}</div>
{%- if winner.info -%}<br>{{winner.info}}{%- endif -%}
</div>
{% endfor %}
{%endfor%}
</section>
