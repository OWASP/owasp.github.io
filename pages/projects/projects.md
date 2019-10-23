---

layout: col-sidebar
title: Projects
permalink: /projects
site_side: true
tags: projects

---

## Welcome to the OWASP Global Projects Page

An OWASP project is a collection of related tasks that have a defined roadmap and team members. OWASP project leaders are responsible for defining the vision, roadmap, and tasks for the project. The project leader also promotes the project and builds the team. OWASP currently has 'over '93' active projects', and new project applications are submitted every week.

Why?

This is one of the most popular divisions of OWASP as it gives members an opportunity to freely test theories and ideas with the professional advice and support of the OWASP community. Every project has an associated mail list. You can view all the lists, examine their archives, and subscribe to any project by visiting the OWASP Project Mailing Lists page. A summary of recent project announcements is available on the OWASP Updates page.

Download the OWASP Project Handbook 2014

Or read the wiki version: OWASP Project Handbook Wiki 2014

Project Online Resources

## Who Should Start an OWASP Project?
* Application Developers.
* Software Architects.
* Information Security Authors.
* Those who would like the support of a world wide professional community to develop or test an idea.
* Anyone wishing to take advantage of the professional body of knowledge OWASP has to offer.

Fund Information
https://www.owasp.org/index.php/Funding

OWASP Project Inventory
All OWASP tools, document, and code library projects are organized into the following categories:

<strong>Flagship Projects:</strong> The OWASP Flagship designation is given to projects that have demonstrated strategic value to OWASP and application security as a whole.
<strong>Lab Projects:</strong> OWASP Labs projects represent projects that have produced an OWASP reviewed deliverable of value.
<strong>Incubator Projects:</strong> OWASP Incubator projects represent the experimental playground where projects are still being fleshed out, ideas are still being proven, and development is still underway.

<div class='projects-list'>
    <h2>List of Projects by <a id="projects-level" class='active'>Level</a> or <a id="projects-type" class='inactive'>Type</a></h2>
    <div id="project-list-level" class='project-list'>
        {% assign fs_projects = site.data.projects | where:'level', '4' %}
        {% assign l_projects = site.data.projects | where:'level', '3' %}
        {% assign i_projects = site.data.projects | where:'level', '2' %}
        {% assign u_projects = site.data.projects | where:'level', '-1' %}
        <h2>Flagship Projects <img src='https://www2.owasp.org/assets/images/common/owasp_level_flagship.svg' width='45px' alt='Flagship'></h2>
        {% for project in fs_projects %}
        <p><a href="{{ project.url }}">OWASP {{ project.name }}</a></p>
        {% endfor %}
        <h2>Lab Projects <img src='https://www2.owasp.org/assets/images/common/owasp_level_labs.svg' width='45px' alt='Lab'></h2>
        {% for project in l_projects %}
        <p><a href="{{ project.url }}">OWASP {{ project.name }}</a></p>
        {% endfor %}
        <h2>Incubator Projects <img src='https://www2.owasp.org/assets/images/common/owasp_level_incubator.svg' width='45px' alt='Incubator'></h2>
        {% for project in i_projects %}
        <p><a href="{{ project.url }}">OWASP {{ project.name }}</a></p>
        {% endfor %}
        <h2>Projects Needing Website Update</h2>
        {% for project in u_projects %}
        <p><a href="{{ project.url }}">OWASP {{ project.name }}</a></p>
        {% endfor %}
    </div>
    <div id="project-list-type" style='display:none;'>
        {% assign tool_projects = site.data.projects | where:'type', 'tool' %}
        {% assign documentation_projects = site.data.projects | where:'type', 'documentation' %}
        {% assign code_projects = site.data.projects | where:'type', 'code' %}
        {% assign other_projects = site.data.projects | where:'type', 'other' %}
        <h2>Tool Projects<i style="margin-left:12px;" class="fa fa-tools fa-lg"></i></h2>
        {% for project in tool_projects %}
        <p><a href="{{ project.url }}">OWASP {{ project.name }}</a></p>
        {% endfor %}
        <h2>Documentation Projects<i style="margin-left:12px;" class="fa fa-file-pdf fa-lg"></i></h2> 
        {% for project in documentation_projects %}
        <p><a href="{{ project.url }}">OWASP {{ project.name }}</a></p>
        {% endfor %}
        <h2>Code Projects<i style="margin-left:12px;" class="fa fa-file-code fa-lg"></i></h2>
        {% for project in code_projects %}
        <p><a href="{{ project.url }}">OWASP {{ project.name }}</a></p>
        {% endfor %}
        <h2>Other Projects</h2>
        {% for project in other_projects %}
        <p><a href="{{ project.url }}">OWASP {{ project.name }}</a></p>
        {% endfor %}
    </div>
</div>
<script type="text/javascript">
    $(function(){
        $('#projects-type').click(function(){
            $('#project-list-level').hide();
            $('#project-list-type').show();
            $('#projects-level').removeClass('active');
            $('#projects-type').addClass('active');
            $('#projects-level').addClass('inactive');
            $('#projects-type').removeClass('inactive');
        });
        $('#projects-level').click(function(){
            $('#project-list-type').hide();
            $('#project-list-level').show();
            $('#projects-type').removeClass('active');
            $('#projects-level').addClass('active');
             $('#projects-level').removeClass('inactive');
            $('#projects-type').addClass('inactive');
        });
    });
</script>

   
