---

layout: full-width
title: Generic Page Example Title
permalink: /corporate

---

## About OWASP

Every vibrant technology marketplace needs an unbiased source of information on best practices as well as an active body advocating open standards. In the Application Security space, one of those groups is the Open Web Application Security Project™ (or OWASP for short).

The Open Web Application Security Project (OWASP) is a 501(c)(3) worldwide not-for-profit charitable organization focused on improving the security of software. Our mission is to make software security visible, so that individuals and organizations are able to make informed decisions. OWASP is in a unique position to provide impartial, practical information about AppSec to individuals, corporations, universities, government agencies, and other organizations worldwide. Operating as a community of like-minded professionals, OWASP issues software tools and knowledge-based documentation on application security.

Everyone is free to participate in OWASP and all of our materials are available under a free and open software license. You'll find everything about OWASP here on or linked from our wiki and current information on our OWASP Blog. OWASP does not endorse or recommend commercial products or services, allowing our community to remain vendor neutral with the collective wisdom of the best minds in software security worldwide.

We ask that the community look out for inappropriate uses of the OWASP brand including use of our name, logos, project names, and other trademark issues.

There are thousands of active wiki users around the globe who review the changes to the site to help ensure quality. If you're new, you may want to check out our getting started page. As a global group of volunteers with over 45,000 participants, questions or comments should be sent to one of our many mailing lists focused on a topic or directed to the staff using the OWASP Contact Us Form.

## OWASP Foundation Staff
|   |   |
|---|---|
{% for member in site.data.staff %}
|<div style="display:table-cell;background-image: url({{ member.image }});background-size:contain;width:150px;height:180px; background-repeat: no-repeat;"></div>|	
        <div style="display:tabel-cell;float:left;padding-left:8px;"><span style="font-weight:bold;">{{ member.name }}<br/>{{ member.title }}</span><p>{{ member.description }}</p></div>|	
{% endfor %}	
