---

layout: col-sidebar
title: Opinions & News
permalink: /news/

---

Weekly news and opinions from OWASP leadership, staff, and community members. Have an idea you'd like to see here?  [Submit to News](mailto:news@owasp.com?subject=News%20Idea) today!
  
<section class="homepage-blog">
{% assign posts = site.posts | limit: 100 %}
{% for post in posts %} <!-- reversed -->
<hr>
<h2><a href="{{ post.url }}">{{ post.title }}</a></h2>
<a><img src="{{ post.author_image }}" alt="image"></a>
<p class="author"><a>{{ post.author }}</a></p>
<p>{{ post.date | date: "%A, %B %e, %Y" }} {{ post.excerpt }}<a href="{{ post.url }}">... more</a></p>
{% endfor %}
</section>
