---

title: Discounted Regions for Membership
layout: col-generic
tags: membership, membership discounts
permalink: /membership/discounts/

---

## The following regions currently qualify for discounted membership:

{% assign discounted = site.data.countries | where: 'discount', true %}
{% for country in discounted %}
* {{ country.name }}
{% endfor %}
