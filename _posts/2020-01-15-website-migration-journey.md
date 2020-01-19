---

date:   2020-01-15
categories: Website
author: Mike McCamon
author_image: /assets/images/people/staff_mike.jpg
layout: blogpost
title: Our Website Migration Journey
excerpt_separator: <!--more-->

---
For the better part of the last nine months, a small dedicated team has been working to complete a project that has been started, restarted, abandoned, restarted, and then again abandoned: migrating our 7,000 or so page website curated by over 3,000 content editors from MediaWiki to GitHub Pages. As I like to now say, “when you spend 15 years digging a deep hole, don’t expect to dig your way our in a week.” And in all honesty this is not the finish line, but the starting line for the OWASP Foundation in this new decade.<!--more-->

Our old website and infrastructure has served us well. But for a good variety of reasons the OWASP Foundation wanted to migrate to a better publishing platform that:
1. More closely aligns with our audience of developers
2. Get our arms around a brittle and broken user credentials model
3. Reduce our costs and maintenance overhead by migrating to a hosted provider
4. Move away from persistent services to static web content thereby vastly increasing the security of our website.

**Audience**. Our audience is developers - mostly web developers. They code, manage, build, and collaborate on tools like GitHub. When we were considering a new CMS the logic was “why not use the tool our audience already uses?”  We added Watch and Star buttons to projects so now when someone searches something like Cross Site Scripting and they find our Cheat Sheet visitors are one click away from connecting to our project - and future updates. We added “Edit on GitHub” links on basically every page so the community, in fact anyone can submit a pull request to change our website. Now that’s open!

<p class="callout-mono right">"When you spend 15 years digging a hole, don’t expect to get out in one week."</p>

**Credentials Management**. Historically we had a very flat content creator credentials model. While it did most often worked to be self-healing, it is not the way to run a website that gets millions of visitors a year.  We elected to silo user credentials by repository and put all ~650 repos in our organizational unit.  Some of our projects do have ongoing code work that needed to be separated from our public-facing web content but the folks working on code also needed access to our “CMS” so co-mingling made a good deal of sense. Each repo, which closely matches for us to each project or local chapter, has it’s own content owners which we authenticate through GitHub.

**Content Architecture**. To oversimplify we have two core repositories for our site - the base site in owasp.github.io and www--site-theme where we host the themes, menus, and data files of the site. There are a few other special repos for staff, our Board, etc but the remainder of our content is in hundreds of repos one for each project or chapter.  Generally the template repo for us has an index and two other key files, leaders and info.  We expect markdown in these files, but allow html, css, scripts, and Jekyll. The site builds automatically when repos are updated (with an expected latency). Some of the most prolific content editors don’t even have a local environment and edit content using GitHub’s web interface on Chromebooks.

<p class="callout-mono left">Automation will allow us to manage and monitor our content in ways we haven't even imagined yet.</p>

**Automation**. Natively on the site, we use a variety of data files (in yml format) and simple Jekyll code to give us some of the content reuse benefits often found in CMS tools like Wordpress. We have also built a variety of scripts that nightly monitor content and rebuilt some of those data files.  For instance, we have a nightly script that monitors which Chapters have yet to migrate their content and write that info to a file that we reuse as a list for management. Crawling our site’s text files is pretty simple code and we have plans for these features going forward.

**Migrating Content**. We’re still not done. Well it has been a nightmare. Our old system allowed pretty much any one of 3,000 editors to stand up a page whenever they wanted. They could upload PDFs, create categories, and basically do whatever they wanted. Some pages had tabs others didn’t - it was a beautiful mess. Harold, our Director of Technology found a few libraries to migrate over most of our wiki markdown to the site but to call it lossy is generous. And when you have lived in the same house for 15 years you accumulate a lot of things that just need to get pitched. We didn’t do that unfortunately. In fact one big project was migrating and then remapping for search redirect were over 1,000 PDFs many of which are out of date. As a backup plan we have parked our old website at wiki.owasp.org but honestly I don’t think **any** website is ever finished.

<p class="callout-mono right">Want to be publicly listed as a supporter of a project or chapter? Yeah we can do that with just a few lines of code.</p>

**Integrating Stripe**. We have found a great developer to help us implement Stripe for our Donations, Membership and soon Event registration. One key requirement was to not have any persistent services running (like a database) and the code needed to be sanitized for credentials since anyone can view our pages. We elected to implement these services using code also running privately on our Azure instance so while the forms are public, the backend verifies transactions and hides sensitive credentials. One fun little feature this design afforded us was the ability to auto populate supporter information on Projects or Chapters. If you are on a Chapter page and you click our Donate button an option appears on the donation form “Please publicly list me as a supporter of x” and if selected our code will place that name into the proper file in that chapter/project repo for public consumption.

**Outstanding Issues**. We have a list of features for Pages. Some critical but most are for convenience. The biggest issue for our community is how Pages publishes security headers.  They know it’s an issue, and I’m confident it’s on the list.

**Final Analysis**. It is my personal view that more groups like us should consider Pages for their CMS. In the post-modern web, content publishing isn’t what is was like 20 years ago and more organizations should recognize it. Also tools and tastes evolve with each new generation of developers and today’s tool is GitHub.
