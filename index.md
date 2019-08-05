---

layout: home
title: Welcome to OWASP
permalink: /

---

<!-- Rebuild Site Tag 47 -->
<section class="homepage-promo">
  <img src="/assets/images/content/group_small.jpg" alt="Volunteers at AppSec">
</section>

<section class="homepage-welcome">
  <h1>What is the OWASP Foundation?</h1>
<p>The Open Web Application Security Project (OWASP) is a nonprofit foundation that works to improve the security of software. Through community-led open source software projects, over 260 local chapters worldwide, tens of thousands of members, and leading educational and training conferences, the OWASP Foundation is the source for developers and technologists to secure the web. Our community provides:</p>

<ul>
<li>Tools and Resources</li>
<li>Community and Networking</li>
<li>Education & Training</li>
</ul>

<p>For nearly two decades corporations, foundations, developers, and volunteers have supported the OWASP Foundation and its work. <a href="#">Donate</a>, <a href="#">Join</a>, or become a <a href="#">Corporate Member</a> today.</p>

  <a href="" class="callout-link">Find a local chapter</a>
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
  <h2><a href="#">New Website Uses GitHub</a></h2>
  <a><img src="https://owasp.github.io/www--site-theme/assets/image/test-photo.png" alt=""></a>
  <p class="author"><a>Joey Michael</a></p>
  <p>Blog post example content. Talk about using GitHub for the new website. More text to follow in a second here. Describe the functionality and the awesome CSS. New blog post example content. Talk about using GitHub for the new website. More text to the awesome CSS. blog post example content. Talk 12345 about using GitHub for the new website. More text to follow in a second here. Tak about uvvsing GitHub for the new website. More text to follow in a second here.  and the awesome CS wordlog ... <a href="#">Read more</a> </p>

</section>

{% include news-events.html %}
