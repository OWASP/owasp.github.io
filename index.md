---

layout: home
title: Welcome to OWASP
permalink: /

---

<!-- Rebuild Site Tag 52 -->
<section class="homepage-promo">
  <img src="/assets/images/content/group_small.jpg" alt="Volunteers at AppSec">
</section>

<section class="homepage-welcome">
  <h1>What is the OWASP Foundation?</h1>
<p>The Open Web Application Security Project (OWASP) is a nonprofit foundation that works to improve the security of software. Through community-led open source software projects, over 260 local chapters worldwide, tens of thousands of members, and leading educational and training conferences, the OWASP Foundation is the source for developers and technologists to secure the web. Join us for:</p>

<ul>
<li>Tools and Resources</li>
<li>Community and Networking</li>
<li>Education & Training</li>
</ul>

<p>For nearly two decades corporations, foundations, developers, and volunteers have supported the OWASP Foundation and its work. <a href="#">Donate</a>, <a href="#">Join</a>, or become a <a href="#">Corporate Member</a> today.</p>

  <a href="https://www.meetup.com/pro/owasp" class="callout-link">Find a local chapter</a>
</section>

<section class="homepage-project">
 {% capture my_include %}{% include featured_project.md %}{% endcapture %}
  {{ my_include | markdownify }}
</section>

<section class="homepage-chapter">
  {% capture my_include %}{% include featured_chapter.md %}{% endcapture %}
  {{ my_include | markdownify }}
</section>

<section class="homepage-blog">
  <h2><a href="#">{{ site.posts.first.title }}</a></h2>
<a><img src="{{ site.posts.first.author_image }}" alt="image"></a>
<p class="author"><a>{{ site.posts.first.author }}</a></p>
<p>{{ site.posts.first.excerpt }}<a href="{{ site.posts.first.url }}">...read more</a></p>
</section>

{% include news-events.html %}
