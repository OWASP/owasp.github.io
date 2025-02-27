---

layout: home
title: OWASP Foundation, the Open Source Foundation for Application Security 
permalink: /
tags: Application Security, Cyber Security, Information Security, Web, Cloud, Vulnerability Assessment
spnews: False

---
<!-- Mastodon verification -->
<link rel="me" href="https://infosec.exchange/@owasp">

<!-- Discoverable Feeds -->
<link rel="alternate" type="application/atom+xml" title="{{ site.title }}" href="{{ "/feed.xml" | prepend: site.baseurl | prepend: site.url }}">
<link rel="alternate" type="application/json" title="{{ site.title }}" href="{{ "/feed.json" | prepend: site.baseurl | prepend: site.url }}"/>
<link rel="alternate" type="application/rss+xml" title="{{ site.title }}" href="{{ "/rss.xml" | prepend: site.baseurl | prepend: site.url }}">

<!-- Rebuild Site Tag 194 -->

<div class="homepage-promo" style='background: url(/assets/images/content/ams-preso-new.jpg) no-repeat center center;background-size: cover;'>
  <!--<img src="/assets/images/content/ams-preso-new.jpg" alt="Presentation at Global AppSec AMS">-->
</div>

 <hr class="mobile">

<section class="homepage-welcome">
</section>

<hr>

{% if page.spnews %}
{% include specialnews.md %}
{% endif %}

<hr class="mobile">

<div style="display:grid;grid-column: 1/3; background-color:#fff;">
  {% include featured_events.html %}  
</div>

<hr>

<section class="homepage-blog">
  <h2><a href="{{ site.posts.first.url }}">{{ site.posts.first.title }}</a></h2>
<a><img src="{{ site.posts.first.author_image }}" alt="image"></a>
<p class="author"><a>{{ site.posts.first.author }}</a><span style="color:#7C7C7C">, {{ site.posts.first.date | date: "%B %e, %Y" }}</span></p>
<p>{{ site.posts.first.excerpt }}<a href="{{ site.posts.first.url }}">...read more</a></p>
</section>

<div style="display:grid;grid-column: 1/3; background-color:#fff;">
 {% include upcoming_owasp.html %}
</div>

<div style="display:grid;grid-column: 1/3; background-color:#fff;">
  {% include flagships.html %}
</div>

<hr class="mobile">

{% include news-events.html %}

<hr class="mobile">
