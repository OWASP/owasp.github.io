---

layout: col-generic
title: OWASP Global & Regional Events
permalink: /events

---
![Attendees at a Global AppSec Conference](/assets/images/web/events-header.png)

Ever wanted to network and learn along with other AppSec professionals? We host nearly a dozen events each year varying in format to week long trainings and conferences, to single day programs. OWASP events are a great way to:

- Improve you career skills
- Build your professional network
- Learn about new trends in the industry

While some of our events have corporate sponsors, the content is vendor neutral, and speakers are carefully selected ensuring a good return on your investment of time and money. Often times are larger events also host Expositions, Capture the Flags, and Career Fairs. Often members get a discount on conference passes.

Skip to <a href="#regionalevents">Regional Events</a> or <a href="#globalpartnerevents">Global Partner Events</a>

## Global Events

Our premier events with up to three days of training followed by a two day conference with keynotes and multiple tracks. A global team plans the agenda, selects the speakers, and hosts the event.

#### Global AppSec Dublin
- June 15-19, 2020
- Registration Opens February 1, 2020
- [https://dublin.globalappsec.org](https://dublin.globalappsec.org)

#### Global AppSec San Francisco
- October 19-23, 2020
- Registration Opens March 1, 2020
- [https://sf.globalappsec.org](https://sf.globalappsec.org)

<a name="regionalevents">
## Regional Events

Ranging from single day to week long events, local OWASP volunteers organize and host conferences around the world. 


{% assign event-list = site.events | sort: 'start-date' | limit: 100 %}
{% for event in event-list %}
 {% if event.type contains 'local' %}
  <h3>{{ event.name }}</h3>
    <ul>
      <li>{{ event.dates }}</li>
      {% if event.optional-text %}<li>{{ event.optional-text }}</li>{% end if %}
      <li>
        <a href='{{ event.url }}' target='_blank'>{{ event.url }}</a></li>
 {% endif %}
{% endfor %}



#### German OWAPS Day 2019
- December 9-10, 2019
- Karlsruhe, Germany
- [https://god.owasp.de/]([https://god.owasp.de/)

#### OWASP Italy Day Udine 2019
- December 14, 2019
- Udine, Italy
- [https://www.owasp.org/index.php/Italy_OWASP_Day_Udine_2019](https://www.owasp.org/index.php/Italy_OWASP_Day_Udine_2019)

**This content will be rendered from a regional-events.yml file

<a name="globalpartnerevents">
## Global Partner Events

Throughout the year, the OWASP Foundation partners with major AppSec conferences to offer discounted tickets and other benefits for OWASP members. If you would like to establish a global partnership with us please contact [Partnership Marketing](mailto:lisa.jones@owasp.com?subject=Partnership%20Marketing) for more information.

#### BlackHat Europe
- December, 2-5, 2019
- London, England
- € 200.00 discount code available
- [Registion Site](https://www.blackhat.com/eu-19/?_mc=sem_x_bheur_le_tsnr_bheu_x_goog_x-BHEU2019Beu&ppc=y&kw=x&gclid=EAIaIQobChMI7M7t_9im5QIVAj0MCh1kDAAlEAAYASAAEgK18vD_BwE)
