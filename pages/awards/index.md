---

title: Achievements and Awards
layout: col-sidebar
permalink: /awards/
tags: awd

---

OWASP recognizes the significant work that our volunteer community contributes regularly to help OWASP achieve its mission and remain a world leader in application security. OWASP 
grants financial and non-financial awards based on merit and community involvement. The following are current OWASP award initiatives:

{% assign categories = site.data.awards | where: 'type', 'category' %}
{% for category in categories %}
### {{category.title}}
{{category.description}}
{% endfor %}