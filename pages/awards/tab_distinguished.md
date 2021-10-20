---

title: Distinguished
displaytext: Distinguished Lifetime
layout: null
tab: true
order: 1
tags: awd

---

## Distinguished Lifetime Membership Awards
<section class="corporate">

{% assign awards = site.data.awards | where: 'category', 'Distinguished Lifetime' | sort: 'year' | reverse %}
{% assign previous = nil %}
{%for award in awards %}
{% if previous != award.year %}
{% assign previous = award.year %}
<hr>
<h2>{{award.year}}</h2>
{% endif %}
{% for winner in award.winners %}
<div class="member-container">
{% if winner.image %}<div class="member-img-container"><img src="{{winner.image}}" alt="{{winner.name}}" class="member-img"></div>{% endif %}<div class="member-caption"><h3>{{ winner.name }}</h3>{%if winner.title %}({{winner.title}}){% endif %}</div>
{%- if winner.info -%}<br>{{winner.info}}{%- endif -%}
</div>
{% endfor %}
{%endfor%}
</section>