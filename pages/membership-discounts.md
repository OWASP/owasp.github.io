---

title: Discounted Regions for Membership
layout: col-sidebar
tags: membership, membership discounts

---

## The following regions currently qualify for discounted membership:

{% assign discounted = site.data.countries | where: 'discount', True %}
{% for country in discounted %}
* {{ country.name }}
{% endfor %}
