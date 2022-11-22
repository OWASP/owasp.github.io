---

layout: col-sidebar
title: Other Projects
permalink: /other_projects/
site_side: true
tags: projects

---

<strong>Lab Projects:</strong> OWASP Labs projects represent projects that have produced an OWASP reviewed deliverable of value.<br>
<strong>Incubator Projects:</strong> OWASP Incubator projects represent the experimental playground where projects are still being fleshed out, ideas are still being proven, and development is still underway.

{% assign l_projects = site.data.projects | where:'level', '3' | where_exp: "project", "project.build != 'no pages'" %}
{% assign i_projects = site.data.projects | where:'level', '2' | where_exp: "project", "project.build != 'no pages'" %}
{% assign u_projects = site.data.projects | where:'level', '-1' | where_exp: "project", "project.build != 'no pages'" %}

<div id="project-list-level" class='project-list'>
        {% assign fs_projects = site.data.projects | where:'level', '4' | where_exp: "project", "project.build != 'no pages'" %}
        {% assign p_projects = site.data.projects | where:'level', '3.5' | where_exp: "project", "project.build != 'no pages'" %}
        
        <p>
        </p>
        <h3>Lab Projects <span class="fa-stack fa-2x">
        <i class="fas fa-circle fa-stack-2x" style="color:#FFA500"></i>
        <i class="fas fa-flask fa-stack-1x fa-inverse"></i>
        </span></h3>
        <ul>
        {% for project in l_projects %}
        <li><a href="{{ project.url }}">{{ project.title }}</a></li>
        {% endfor %}
        </ul>
        <h3>Incubator Projects <span class="fa-stack fa-2x">
        <i class="fas fa-circle fa-stack-2x" style="color:#53AAE5"></i>
        <i class="fas fa-egg fa-stack-1x fa-inverse"></i>
        </span></h3>
        <ul>
        {% for project in i_projects %}
        <li><a href="{{ project.url }}">{{ project.title }}</a></li>
        {% endfor %}
        </ul>
        <h3>Projects Needing Website Update</h3>
        <ul>
        {% for project in u_projects %}
        <li><a href="{{ project.url }}">{{ project.title }}</a></li>
        {% endfor %}
        </ul>
    </div>