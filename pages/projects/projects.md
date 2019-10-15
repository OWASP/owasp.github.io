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

## Alphabetical List of All Projects

<div id="project-list">
</div>

<script type="text/javascript">
    var repoNames = [{% for repo in site.github.public_repositories %}{% if repo.has_pages and repo.name contains "www-project-" %}{% assign repoName = repo.name | slice: 12, 199 | split: "-"  %}{% capture repoNameCase %}{% for word in repoName %}{{ word | capitalize | append: " " }}{% endfor %}{% endcapture %}
            "{{ repoNameCase }}"{% unless forloop.last %}, {% endunless %}{% endif %}{% endfor %}];
    var repoUrls = [{% for repo in site.github.public_repositories %}{% if repo.has_pages and repo.name contains "www-project-" %}"https://www2.owasp.org/{{ repo.name }}"{% unless forloop.last %}, {% endunless %}{% endif %}{% endfor %}];

    var githubUrls = [{% for repo in site.github.public_repositories %}{% if repo.has_pages and repo.name contains "www-project-" %}"https://api.github.com/v3/repos/owasp/{{ repo.name }}/contents/index.md"{% unless forloop.last %}, {% endunless %}{% endif %}{% endfor %}];

    $(function () {
        var htmlstring = "";
        $.each(repoNames, function(index){
            htmlstring += "<a href=" + repoUrls[index] + ">" + repoNames[index];
            $.get(githubUrls[index]).done(function (data) {
                var contents = atob(data["contents"]);
                var levelStr = "No level";
                if(contents.indexOf("level:") >= 0)
                {
                    var level = parseInt(contents.substring(contents.indexOf("level:") + 6, 1));
                    switch(level)
                    {
                        case 1:
                            lavelStr = "Inactive";
                            break;
                        case 2:
                            levelStr = "Incubator";
                            break;
                        case 3:
                            levelStr = "Lab";
                            break;
                        case 4:
                            levelStr = "Flagship";
                            break;
                    }
                }
                htmlstring += levelString;
            });
            htmlstring += "</a><br/>";
        });     
        //note that the above is not synchronous so this will not work

        $("#project-list").html(htmlstring);
    });
</script>