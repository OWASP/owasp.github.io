---

layout: home
title: OWASP Foundation, the Open Source Foundation for Application Security 
permalink: /
tags: Application Security, Cyber Security, Information Security, Web, Cloud

---

<!-- Rebuild Site Tag 122 -->

<div class="homepage-promo">
  <img src="/assets/images/content/ams-preso-new.jpg" alt="Presentation at Global AppSec AMS">
</div>

 <hr class="mobile">

<section class="homepage-welcome">
  <h1>Who is the OWASP Foundation?</h1>
<p>The Open Web Application Security Project (OWASP) is a nonprofit foundation that works to improve the security of software. Through community-led open source software projects, hundreds of local chapters worldwide, tens of thousands of members, and leading educational and training conferences, the OWASP Foundation is the source for developers and technologists to secure the web.</p>

<ul>
<li>Tools and Resources</li>
<li>Community and Networking</li>
<li>Education & Training</li>
</ul>

<p>For nearly two decades corporations, foundations, developers, and volunteers have supported the OWASP Foundation and its work. <a href="/donate/">Donate</a>, <a href="/membership/">Join</a>, or become a <a href="/supporters">Corporate Member</a> today.</p>
</section>

<hr>

<section class="homepage-project">
 {% capture my_include %}{% include featured_project.md %}{% endcapture %}
  {{ my_include | markdownify }}
</section>

<hr class="mobile">

<section class="homepage-chapter">
  {% capture my_include %}{% include featured_chapter.md %}{% endcapture %}
  {{ my_include | markdownify }}
</section>

<hr>

<section class="homepage-blog">
  <h2><a href="{{ site.posts.first.url }}">{{ site.posts.first.title }}</a></h2>
<a><img src="{{ site.posts.first.author_image }}" alt="image"></a>
<p class="author"><a>{{ site.posts.first.author }}</a><span style="color:#7C7C7C">, {{ site.posts.first.date | date: "%B %e, %Y" }}</span></p>
<p>{{ site.posts.first.excerpt }}<a href="{{ site.posts.first.url }}">...read more</a></p>
</section>

<hr class="mobile">

{% include news-events.html %}
