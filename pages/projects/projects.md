---

layout: col-sidebar
title: Projects
permalink: /projects
site_side: true
tags: projects

---

![Global Board Class of 2019](/assets/images/web/juice-shop.png)

## Projects for Good

we are a community of developers, technologists and evangelists improving the security of softare. The OWASP Foundation gives aspiring open source projects a plaform to secure the web with:
- Visibility: Our website gets more than six million visitors a year
- Credibility: OWASP is well known in the AppSec community
- Resources: Funding and Project Summits are available for qualifying Programs
- Community: Our Conferences and Local Chapter Meetings connect your project

<p class="callout-mono right">Together we will improve the security of software.</p>

OWASP Projects are a collection of related tasks that have a defined roadmap and team members. OWASP project leaders are responsible for defining the vision, roadmap, and tasks for the project. The project leader also promotes the project and builds the team. OWASP currently has 'over '93' active projects', and new project applications are submitted every week.

Projects gives members an opportunity to freely test theories and ideas with the professional advice and support of the OWASP community. Every project minimally has their own webpage, mailing list, and Slack Channel.

## Who Should Start an OWASP Project?
- Application Developers
- Software Architects
- Information Security Authors
- Those who would like the support of a world wide professional community to develop or test an idea.

## OWASP Project Inventory
All OWASP tools, document, and code library projects are organized into the following categories:

<strong>Flagship Projects:</strong> The OWASP Flagship designation is given to projects that have demonstrated strategic value to OWASP and application security as a whole.<br>
<strong>Lab Projects:</strong> OWASP Labs projects represent projects that have produced an OWASP reviewed deliverable of value.<br>
<strong>Incubator Projects:</strong> OWASP Incubator projects represent the experimental playground where projects are still being fleshed out, ideas are still being proven, and development is still underway.

<div id='all-projects' class='projects-list'>
    <h3>List of Projects by <a id="projects-level" class='active'>Level</a> or <a id="projects-type" class='inactive'>Type</a></h3>
    <div id="project-list-level" class='project-list'>
        {% assign fs_projects = site.data.projects | where:'level', '4' %}
        {% assign l_projects = site.data.projects | where:'level', '3' %}
        {% assign i_projects = site.data.projects | where:'level', '2' %}
        {% assign u_projects = site.data.projects | where:'level', '-1' %}
        <h3>Flagship Projects <img src='https://www2.owasp.org/assets/images/common/owasp_level_flagship.svg' width='45px' alt='Flagship'></h3>
        <ul>
        {% for project in fs_projects %}
        <li><a href="{{ project.url }}">OWASP {{ project.name }}</a></li>
        {% endfor %}
        </ul>
        <h3>Lab Projects <img src='https://www2.owasp.org/assets/images/common/owasp_level_labs.svg' width='45px' alt='Lab'></h3>
        <ul>
        {% for project in l_projects %}
        <li><a href="{{ project.url }}">OWASP {{ project.name }}</a></li>
        {% endfor %}
        </ul>
        <h3>Incubator Projects <img src='https://www2.owasp.org/assets/images/common/owasp_level_incubator.svg' width='45px' alt='Incubator'></h3>
        <ul>
        {% for project in i_projects %}
        <li><a href="{{ project.url }}">OWASP {{ project.name }}</a></li>
        {% endfor %}
        </ul>
        <h3>Projects Needing Website Update</h3>
        <ul>
        {% for project in u_projects %}
        <li><a href="{{ project.url }}">OWASP {{ project.name }}</a></li>
        {% endfor %}
        </ul>
    </div>
    <div id="project-list-type" style='display:none;'>
        {% assign tool_projects = site.data.projects | where:'type', 'tool' %}
        {% assign documentation_projects = site.data.projects | where:'type', 'documentation' %}
        {% assign code_projects = site.data.projects | where:'type', 'code' %}
        {% assign other_projects = site.data.projects | where:'type', 'other' %}
        <h2>Tool Projects<i style="margin-left:12px;" class="fa fa-tools fa-lg"></i></h2>
        <ul>
        {% for project in tool_projects %}
        <li><a href="{{ project.url }}">OWASP {{ project.name }}</a></li>
        {% endfor %}
        </ul>
        <h2>Documentation Projects<i style="margin-left:12px;" class="fa fa-file-alt fa-lg"></i></h2>
        <ul> 
        {% for project in documentation_projects %}
        <li><a href="{{ project.url }}">OWASP {{ project.name }}</a></li>
        {% endfor %}
        </ul>
        <h2>Code Projects<i style="margin-left:12px;" class="fa fa-file-code fa-lg"></i></h2>
        <ul>
        {% for project in code_projects %}
        <li><a href="{{ project.url }}">OWASP {{ project.name }}</a></li>
        {% endfor %}
        </ul>
        <h2>Other Projects</h2>
        <ul>
        {% for project in other_projects %}
        <li><a href="{{ project.url }}">OWASP {{ project.name }}</a></li>
        {% endfor %}
        </ul>
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
