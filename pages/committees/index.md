---

title: OWASP Committees
layout: col-sidebar
permalink: /committees/
tags: committees

---

OWASP Committees provide an opportunity to directly impact the future of the OWASP Foundation. As a committee member you are the voice for focus areas and represent the OWASP community around the world. The committees design a committee plan to focus on specific areas of improvement within their domain. OWASP Committees are governed under the [OWASP Committee 2.0 policy](/www-policy/operational/committees.html).


<p class="callout-mono left">Represent the OWASP Community around the world.</p>

To encourage focus and participation, we recommend that volunteers contribute to one primary committee. Individuals are welcome to participate in whatever committee they would like but may only be officially elected to serve on one committee.

### List of Committees

<ul>
{% for comm in site.data.committees %}
    <li><a href='{{ comm.url }}'>{{ comm.title }}</a></li>
{% endfor %}
</ul>