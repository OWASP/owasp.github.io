---

layout: col-generic
title: OWASP Staff
permalink: /corporate/

---

<h2>Staff</h2>
<p>
Under the direction of the Executive Director, staff implements programs and policies of the Foundation while collaborating with members on OWASP Projects, Chapters, Events, and initiatives.</p>
<p>
Each year the staff works with the Global Board to establish an <a href="https://owasp.org/www-staff/operating-plan/2022/">Operating Plan</a> and Budget. The work efforts of our staff are tracked publicly at the <a href="/www-staff/operating-plan/2021/status-2021">Operating Plan Status</a>.
</p>

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


