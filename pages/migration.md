---

layout: full-width
title: Website Migration
permalink: /migration/

---

# Website Migration Information and Tutorial

## Getting your page online is as easy as 1-2-3!
1. Re-think your page design. The new template has a handy right column for general info (like links to Chapter Meetings or Code Repos) and you leadership team. We have also implemented a tabbed interface that might allow you to shorten you page length. The site is now responsive so think about that use case as well.
2. We had considered writing a migration tool but our experience has been that copy/paste/edit is about as fast. Wiki and Git markdown are similar so we have been using the Edit feature of the Wiki to copy the content, and then paste into the index.md file knowing you'll have some light editing. (You would have had to do some light editing even with a migration tool).
3. Commit your Changes and Debug. Our expectation is your migration will likely take around 30 mins to a few hours. It is work, and it is a pain, but wow, the new website will be SO much better at encouraging new visitors to join our community and your chapter/project!
4. **Bonus** If you scroll to the botton of the content area of (any) page of the new website you will see a "Edit on Github" link. So check out how others are building their page. Cheat and steal their good ideas.

## Ready to Get Started

Each project and chapter will have their own repository located in the organization repo (https://github.com/OWASP).  The naming convention for repos is: 

**www-project-[projectname or abbreviation]** for projects

**www-chapter-[chaptername]** for chapters.

If you do not have access to your repository yet, please contact [Harold Blankenship](mailto://harold.blankenship@owasp.com)

The following files are included in the repository.  Only the index.md, leaders.md, and info.md files are required:

<span style="color:red;font-weight:bold;">index.md</span>: Contains the main page description of your project or chapter<br/>
<span style="color:darkorchid;font-weight:bold;">leaders.md</span>: Contains the leaders’ names and email addresses.<br/>
<span style="color:lime;font-weight:bold;">info.md</span>: At-a-glance info displayed in the right sidebar (links, project level, etc)<br/>
<span style="color:magenta;font-weight:bold;">tab_[tabname].md</span>: Optional files for tabbed structure if you wish to use them.<br/>

Examples of all these files can be found in 

* [Project-Chapter Example](https://github.com/owasp/www-projectchapter-example)
* [OWASP ZAP](https://github.com/owasp/www-project-zap)
* [OWASP MSTG](https://www2.owasp.org/www-project-mobile-security-testing-guide)
* [OWASP London](https://www2.owasp.org/www-chapter-london)


The following screenshot depicts the website and what areas each of these files affect:

![Image of Website](/assets/images/zap_project_areas.png)

Each file is a Github Flavored Markdown file and can be edited using markdown syntax, HTML syntax, or some combination of the two (though combining HTML and markdown has some pitfalls).  It is recommended that you use Markdown when making edits.  For more information about Markdown, see [https://guides.github.com/features/mastering-markdown/](https://guides.github.com/features/mastering-markdown/)

## INDEX.MD

At the very top of your index.md should be a section that looks like the following:
```
---

layout: col-sidebar
title: <Page Title>
tags: <tags>
level: <level>

---
```

This is called ‘front matter’ and should be the very first thing in your index.md file.  The layout should not be changed and should always be col-sidebar.  The title should be the name of your OWASP chapter or project.  Or instance, the ZAP project would have OWASP Zap as the title.  For tags, these are currently used to associate your tabs with the index.md file that exist on (more on this later).  If you intend to use tabs, you should use a simple word here (e.g. OWASP Zap has tags:zap).  Finally, the level tag can be removed for non-projects.  For projects, the level should be one of: 4 (Flagship), 3 (Lab), or 2 (Incubator).


## LEADERS.MD

The leaders.md file should contain the Leaders header and the names and email addresses of the leaders of the chapter or project.  For example:
```
### Leaders
* [Jenny Leader](mailto://jenny.leader@owasp.org)
* [Calliope Leader](mailto://calliope.leader@owasp.org)
```

When you add or change leaders this file should be kept updated.

## INFO.MD

The info.md file contains the information that will be displayed below the OWASP Foundation information in the sidebar to the right of your page.  This information should contain information similar to that in your Project About on the wiki.  Examples of well-formatted and informational info.md files can be found at

* [https://github.com/owasp/www-project-zap](https://github.com/owasp/www-project-zap)
* [https://github.com/owasp/www-chapter-london](https://github.com/owasp/www-chapter-london)
* [https://www2.owasp.org/www-project-mobile-security-testing-guide](https://www2.owasp.org/www-project-mobile-security-testing-guide)

## TAB_[TABNAME].MD

The tab files are purely optional if you wish to display multiple informational links near the top of your page.  There are other ways to accomplish something similar including just adding your own links to external pages.  The tab structure here is provided to mirror what was available on the wiki.

In order to have tabs work correctly, the [TABNAME] portion of the filename should match the lowercase title in the front matter of the file.  The title cannot contain spaces.  For instance, the tab_supporters.md file in the [OWASP Zap](https://github.com/owasp/www-project-zap) repository has the title: Supporters.  The front matter of that file is included below as an example:
```
---
title: Supporters
displaytext: Our Supporters
layout: null
tab: true
order: 4
tags: zap
---
```

The second item, displaytext is optional.  If displaytext is missing then the title will be displayed as the text of the tab on the page.  Otherwise, the displaytext (which can contain spaces) will be used for the text of the tab.
Of special note is the layout front matter.  This must be null for tab files and putting anything else there can result in some very strange behavior.  

The tab front matter must be set to true and the order indicates what position the tab should take in the tabs displayed on the screen.  Finally, and importantly, the tags front matter must contain the tag that was used in the index.md file mentioned previously or the tab will not display.  Please see the aforementioned repository links for examples.
