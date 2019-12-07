---

layout: col-generic
title: Board and Staff
permalink: /corporate

---

<img src="/assets/images/web/board.png" alt="Global Board Class of 2019">

The OWASP Foundation Global Board is comprised of seven elected members who serve for two-year terms. Each Fall, membership votes to elect new leadership for the Foundation. Generally our Board meets monthly and meetings are open to the public. The Global Board sets the strategic direction of the Foundation, its policies, and sets governance and leadership roles. 

Pictured above is the Global Board Class of 2019. From left to right: [Martin Knobloch, Chair]((mailto:martin.knobloch@owasp.org), [Sherif Mansour, Treasurer]((mailto:sherif.mansour@owasp.org), [Owen Pendlebury, Vice Chair]((mailto:owen.pendlebury@owasp.org), [Richard Greenberg, Member at Large]((mailto:richard.greenberg@owasp.org), [Gary Robinson, Member at Large]((mailto:gary.robinson@owasp.org), [Ofer Maor, Secretary]((mailto:ofer.maor@owasp.org), [Chengxi Wang, Member at Large]((mailto:chengxi.wang@owasp.org), 

n## Staff

Under the direction of the Executive Director, staff implement programs and policies of the Foudation while collaborating with members on OWASP Projects, Chapters, Events, and initiatives.

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


<h2>Board of Directors</h2>


<section id="board" class="corporate">
<div>	
 {% for member in site.data.board %}
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
