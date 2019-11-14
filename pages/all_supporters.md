---

layout: col-blogsidebar
title: Corporate Supporters
permalink: /supporters

---

_Disclaimer:_ The following information is not an endoresement for any particular entity and reflects the messaging of the supporter only.


{% for supporter in site.data.corp_members %}
![{{ supporter.name }}]({{ supporter.image }}){:width="200px"}

{{ supporter.description }}
{% endfor %}


