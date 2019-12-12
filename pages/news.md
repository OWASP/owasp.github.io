---

layout: col-generic
title: Opinions & News
permalink: /news

---

## Opinions & News

Check back here for weekly news and opinions from OWASP leadership, staff, and community members.
  
{% for post in site.posts | limit: 100 %} <!-- reversed -->
  
    <h2><a href="{{ post.url }}">{{ post.title }}</a></h2>
    <a><img src="{{ post.author_image }}" alt="image"></a>
    <p class="author"><a>{{ post.author }}</a></p>
    <p>({{ post.date }}), {{ post.excerpt }}<a href="{{ post.url }}">... more</a></p>
    <hr>
{% endfor %}	
