---

date: 2023-10-03 00:00:00-0700
categories: blog
author: Rose Pezzuti Dyer
author_image: /assets/images/people/pezzdyer.png
layout: blogpost
title: Search Results Pollution
pitch: Bad actors can take advantege of your site's embedded Google search results, but there are ways to control how your site is indexed.
excerpt_separator: <!--more-->

---

# Search Results Pollution

A vulnerability with embedding Google search results on your web site has [recently appeared in the news](https://www.businessinsider.com/google-loophole-buying-drugs-online-hijack-website-2023-9?op=1). This has been an exploit for a while and there are some ways to prevent it and fix an existing problem.

## How are search results polluted?

Any web site that displays a user's unfiltered search term may be inadvertently hosting nefarious content and allowing Google to index it.

Let's say you have a web site that lets users search your pages using Google. Your search result page displays results from pages in your own site that Google has indexed. This page also shows a "you searched for" block above the results which shows the user's search term. 

This is innocuous when the search term pertains to your web site (e.g., "where can I adopt a puppy" or "where can I find cancer treatment"). 

<img width="400" alt="search term looking for cancer treatment, results blurred" src="https://github.com/pzzd/pzzd.github.io/assets/5471867/7484411c-e094-478b-9982-478e13065bef">

But it is nefarious when the search term has explicit information that a bad actor means to have indexed by Google. To a Google bot, it appears that your site is hosting this nefarious content, and your site will show as the source of this information in Google search results.

<img width="400" alt="search term offering to sell drugs" src="https://github.com/pzzd/pzzd.github.io/assets/5471867/98b46d3b-6459-4a9d-a534-124c8cceb08d">

Note that the indexable content is the search term. The search itself does not have to be successful or return any results.

I don't know the exact mechanism a bad actor would use to index such content. It is likely possible by making a web page with links to search results on other sites.

## How can search result pollution be prevented?

The most effective way to prevent search result pollution is to not write out a user's search term. Even Google does not show a user's search term outside of the search input element.

Another way to prevent the problem is to add a robots.txt file to your web site that tells Google not to crawl the search results page:
```
User-agent: *
Disallow: /my-search-page/
```
You can use an [alternative to a robots.txt file](https://developers.google.com/search/docs/crawling-indexing/block-indexing), too.

This approach is no guarantee, though: it relies on Google to honor the disallow rule. If Google decides to ignore your disallow rule, your site will be vulnerable.

## How can a mess be cleaned up?

After blocking the Google bot from your search page and removing the element writing out a user's search term, send a [page removal request to Google](https://developers.google.com/search/docs/crawling-indexing/remove-information?sjid=7470165266361020733-NA&visit_id=638319351474913089-3909863057&rd=1). This part is a moving target as Google changes the tools and rules around such requests now and then. Good luck!
