---

layout: col-blogsidebar
title: Corporate Supporters
permalink: /supporters

---

---
_Disclaimer:_ The following information is not an endorsement for any particular entity and reflects the messaging of the supporter only.

---

{% assign supporters = site.data.corp_members %}

{% for supporter in supporters %}
{% if supporter.sponsor %}
{% assign level = site.data.sponsor_levels | where: 'level', supporter.sponsor | first %}
{% else %}
{% assign level = '' %}
{% endif %}
{% assign wstr = '200px' %}
{% assign hstr = 'auto' %}
{% if supporter.vertical == true %} {% assign wstr = 'auto' %}{% assign hstr = '75px' %}{% endif %}
| [![{{ supporter.name }}]({{ supporter.image }}){:width='{{ wstr }}' height='{{ hstr }}'}]({{ supporter.url }}){:rel="noopener sponsored" target="_blank"}{% if supporter.member %} | ![](/assets/images/member.png){:width="65px"} {% endif %} ![]({{ level.image }}){:width="65px"} |

{{ supporter.description }}
{% endfor %}
