## Past Project Spotlights

{% assign spages = site.pages | where_exp: "page", "page.tags contains page.document" | sort: "order" %}

{% assign spotlights = site.pages | where_exp: "page", "page.path contains '/projects/spotlight/historical/'" | sort: "date" | reverse | limit: 30 %}
{%- for spotlight in spotlights -%}
* {{ spotlight.date }} [{{ spotlight.title }}]( {{spotlight.url}} )
{% endfor %} 