---

layout: col-sidebar
title: Job Postings
permalink: /supporters/jobs
site_side: true
tags: corp-supporter, jobs

---

{% assign supporters = site.data.corp_members | sort: 'sortname' %}
{% for supporter in supporters %}
{% if supporter.job_url %}
[![Image]({{ supporter.image }}){:style="max-width:300px;max-height:300px;"}]({{supporter.job_url}})
{% endif %}
{% endfor %}