---

title: OWASP Website Documentation
layout: col-sidebar
permalink: /site-documentation/

---

## Overview

This documentation provides site editors with the information needed to maintain and create content within the OWASP website. The
specific items covered are Layouts, CSS, and conventions used.  

### Website Design

The OWASP Foundation website is hosted on GitHub Pages and, therefore, is generally static in nature.  What this means is that the
content is generated once an item is 'saved' and that it does not change until the next time that the site is generated (usually
preceded by a document change).  There are some cases where content is dynamically generated and for that we use javascript/jQuery.

Because the site is hosted on GitHub, the site uses Jekyll and the Liquid language. The details of Jekyll and Liquid will not be
covered except to demonstrate concepts.  Each of these has excellent documentation of their own which you can view on the 
[Jekyll site](https://jekyllrb.com/docs/) and the [Liquid site](https://shopify.github.io/liquid/).

In actuality, the OWASP Foundation website is a collection of micro-sites; each micro-site is defined by the repository in which the 
content is located.  Every chapter, project, and committee is housed in its own repository.  This allows the Foundation to manage the 
access to each repository separately. 

In general, the website is composed of the following parts:

* [www--site-theme](https://github.com/owasp/www--site-theme): This is the OWASP Foundation theme in use by all of the micro-sites
and houses the layouts, includes, and CSS in use throughout the website.
* [owasp.github.io](https://github.com/owasp/owasp.github.io): This is the 'main' website for the Foundation.  The items housed here 
are the menus, the blogs, and various core pages (including this one).
* [www-board](https://github.com/owasp/www-board): Houses most items pertaining to the OWASP Foundation Global Board.
* [www-policy](https://github.com/owasp/www-policy): Contains the governing policies and procedures in use by the OWASP Foundation
* [www-community](https://github.com/owasp/www-community): Contains community-contributed content similar to the old wiki pages.  This 
includes the [attacks](/www-community/attacks), [vulnerabilities](/www-community/vulnerabilities), and various initiatives like 
[Google Summer of Code](/www-community/gsoc) and [Code Sprint](/www-community/code_sprint).  This repository is open for contributions by
anyone wishing to help spread the OWASP mission.
* [www-projectchapter-example](https://github.com/owasp/www-projectchapter-example): Each project chapter, committee, and similar is
located in its own repository, depending on the type of item it is.  The projectchapter-example is a template repository that contains
examples to help chapters and projects with their own sites.
* Project and Chapter sites are all under a repository with the format www-[chapter or project]-[group-name].  For instance,
[www-project-juice-shop](https://github.com/owasp/www-project-juice-shop) houses the [OWASP Juice Shop project](/www-project-juice-shop)
web pages. 
* Global Events are also under their own repository of the format www-event-[four digit year]-[event-name].  For example, 
[www-event-2020-GlobalAppSecSF](https://github.com/owasp/www-event-2020-GlobalAppSecSF)


## Layouts

The following are the layouts available under the OWASP Foundation Site Theme

* **col-sidebar**: This is the most common layout and it is the expected layout for all projects, chapters, committees, and other pages when another layout is not specifically called for.  The layout includes a right-hand sidebar which attempts to load the info.md and leaders.md files located in the repository.
* **col-generic**: This provides the same layout as col-sidebar, above, except that the info.md and leaders.md files are not included.  This should be used by any page that is not a chapter, project, or committee page and which does not fall under one of the other layouts.
* **blogpost**: An internally used layout for providing layout for the blogs under the News section.
* **col-blogsidebar**: Not currently in use.
* **col-document**: A simple but effective and mobile-friendly document layout that provides navigation between pages. Documents that are stored under a single folder are best served by this layout.
* **col-document-adv**: A more advanced document layout for complex documents.  This is currently under development (July 24, 2020).
* **event**: Event template layout for current OWASP Foundation events.
* **event_noheader**: Event pages not requiring the header.
* **full-width**: A full-width template that removes the sidebars. This template is used on pages that are not meant to be consumed regularly by the public.
* **home**: The layout used on the OWASP Foundation website homepage.

Examples of these layouts can be found throughout the website.

