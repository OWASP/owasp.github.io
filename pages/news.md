---

layout: col-generic
title: Opinions & News
permalink: /news/

---

Check back here for weekly news and opinions from OWASP leadership, staff, and community members. Have a news idea for here or the Connector?  Submit to [News](mailto:news@owasp.com?subject=News%20Idea)
  
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
