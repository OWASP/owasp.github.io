---

layout: col-generic
title: OWASP Staff
permalink: /corporate/

---

## Staff

Under the direction of the Executive Director, staff implements programs and policies of the Foundation while collaborating with members on OWASP Projects, Chapters, Events, and initiatives.

Each year the staff works with the Global Board to establish an [Operating Plan](https://owasp.org/www-staff/operating-plan/2024/) and [Budget](https://owasp.org/www-staff/budget/2024/)


<section id="staff" class="corporate">
<div>	
 {% for member in site.data.staff %}
    <div class="member-container">
        <div class="member-img-container">	
            <div class="member-img" style="background-image: url(/assets/images{{ member.image }});">
            </div>
        </div>
        <div class="member-caption"><h2>{{ member.name }}</h2><hr><strong>{{ member.title }}</strong><br/><div class="member-location">{{member.location}}</div></div><br/>
        <div class="member-info">{{ member.description }}</div>	
    </div>
    <div style="height:18px;"></div>
{% endfor %}	
</div>
</section>
