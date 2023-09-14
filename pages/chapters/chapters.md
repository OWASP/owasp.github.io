---
title: OWASP Local Chapters
layout: col-sidebar
permalink: /chapters/
site_side: true
tags: chapters
---

<!-- rebuild 1 -->

<style>
  .chapterli {
   -webkit-box-sizing: border-box;
   -moz-box-sizing: border-box;
   box-sizing: border-box;
   display: inline-block;
   width   : 24%;
   padding : 15px; /* this will be applied internally, due to 
                      box-sizing property */
   vertical-align: text-top;
}

.chapter-panel {
  background-color: lightgray;
  margin-bottom: 6px;
}
</style>
<img src="/assets/images/web/chaper-wide.jpg" alt="Bay Area Chapter Meeting">

OWASP Local Chapters build community for application security professionals around the world. Our Local Chapter Meetings are **free and open** to anyone to attend so both members and non-members are always welcomed. Local meetings include:

- Training to improve your skills
- Talks relevant to your work
- Networking opportunities

Chapter pages on this site have general information and leader contact info. Local meeting RSVPs are handled through [https://meetup.com/pro/owasp](https://meetup.com/pro/owasp).


<a href="https://meetup.com/pro/owasp" target="_blank" rel="noopener"><button class="cta-button grey">Search using Map</button></a>

<!--
<div>
<label for='chapters-filter'>Filter List:</label>
<input type='text' id='chapters-filter'>
</div>
-->


## Chapter Listing
{% assign countries = site.data.chapters | map: "country" | uniq | sort %}
{% assign chapter_regions = site.data.chapters | map: "region" | uniq | sort%}
{% assign countries_by_region = "" | split: "," %}
{% for region in chapter_regions %}
  {% assign ch_regions = "" | split: "," %}
  {% for chapter in site.data.chapters %}
    {% if region == chapter.region %}
      {% assign ch_regions = ch_regions | push: chapter %}      
    {% endif %}
  {% endfor %}
  {% assign countries_by_region = countries_by_region | push: ch_regions %}
{% endfor %}

{% comment %}
{% assign old_region = "" %}
{% for region in countries_by_region %}
  {%- for ch in region -%}
    <div>{{ch.name}}</div>
  {% endfor %}
{% endfor %}
{% endcomment %}
{% assign supported_regions = site.data.supported_regions | map: "region" %}
{% assign country_header = false %} 
<div class='chapters-list corp_member_div' id='chapters-list'>
    {% for region in chapter_regions %}
      {%- if supported_regions contains region -%}
        {% assign rcount = 0 %}       
        {% for chapter in site.data.chapters %}
          {% if chapter.region == region and chapter.build != 'no pages' %}
            {% assign rcount = rcount | plus: 1 %}
          {% endif %}
        {% endfor %}  
        <button class='accordion' style="margin-bottom: 3px;font-weight: bold; font-size: larger;"> {{ region }} ({{rcount}})</button>
        <div class='panel chapter-panel'>
              {% for country in countries %}
                {% for rchs in countries_by_region %}
                  {% for chapter in rchs %}
                    
                      {% if chapter.region == region and chapter.build != 'no pages' and chapter.country == country%}
                        {% if country_header == false %}
                          {% assign country_header = true %}
                          {% assign country_title = chapter.country %}
                          {% if country_title == "" %}
                          {% assign country_title = "Unknown" %}
                          {% endif %}                          
                          <ul>
                          <h5><a name="{{country_title}}"></a>{{country_title}}</h5>                        
                          <hr>
                        {% endif %}
                          <li class="chapterli">&bull;<a href='{{ chapter.url }}'>{{ chapter.title | remove_first: "OWASP " }}</a></li>
                      {% endif %}                                                                                               
                  {%endfor%}
                {% endfor %}                                 
                {% if country_header == true %}
                  </ul>
                {% endif %}                  
                {% assign country_header = false %}                                              
              {%endfor%}
        </div>
      {%endif%}
    {% endfor %}
</div>


## Chapters in Unsupported Regions
<ul>
{% for chapter in site.data.chapters %}
    {% assign in_region = false %}
    {% for region in site.data.supported_regions %}
        {% if chapter.region == region.region or chapter.region == "Needs Website Update"%}
            {% assign in_region = true %}
        {% endif %}
    {% endfor %}
    {%- if in_region == false and chapter.build != 'no pages' -%}
    <li><a href="{{chapter.url}}">{{chapter.title}}</a> in {{ chapter.region }}</li>
    {% endif %}
{% endfor %}
</ul>

<script type='text/javascript'>
    var all = "{{ site.data.chapters | jsonify | replace: '"', '\"' | replace: '\t', ' ' }}";
    var chapters = JSON.parse(all);
    var default_chapters = "";
    chapters = chapters.sort(function (a, b) {
      if(a.region > b.region) 
        return 1;
      else if(b.region > a.region)
        return -1;
      else
        return 0; 
    });

    function getLeaderEmailsForGroup(inleaders, group_name){
        var emails = 'mailto:';
        for(x = 0; x < inleaders.length; x++)
        {
          if(inleaders[x].group == group_name)
          {
            emails += inleaders[x].email.replace('mailto://','').replace('mailto:','');
            emails += ",";
          }
        }
        emails = emails.substring(0, emails.length - 1);
        return emails;
    }
    
    $("#chapters-filter").keyup(function(e) {
        var code = e.keyCode ? e.keyCode : e.which;
        if (code == 13) {  // Enter keycode
            if(default_chapters == "") {
              default_chapters = $('#chapters-list').html();
            }
            var filter = $('#chapters-filter').val();
            filter = filter.toLowerCase();

            if ( filter.trim() == "") {
              $("#chapters-list").html(default_chapters);
              return; 
            }
            var fchapters = []; 
            
            for(i = 0; i < chapters.length; i++){
              var region = chapters[i].region.toLowerCase();
              var title = chapters[i].title.toLowerCase();
              var country = "";
              if(chapters[i].country) {
                country = chapters[i].country.toLowerCase();
              }
              //var country = chapters[i].country.toLowerCase();//
              if(chapters[i].build != 'no pages' && (filter == '' || region.indexOf(filter) > -1 || title.indexOf(filter) > -1 || country.indexOf(filter) > -1))
              {
                fchapters.push(chapters[i]);
              }
            }
            var html = "<ul>";
            
            for(i = 0; i < fchapters.length; i++){

                  region = fchapters[i].region;
                  html += "<li><a href='" + fchapters[i].url + "'>";
                  html += region + ":" + fchapters[i].title + "</a></li>";
                }
            
            html += "</ul>";
            $('#chapters-list').html(html);
          }          
      });    
      
    $(".accordion").click(function () {
                  $(this).toggleClass("active");
                  if($(this).next('.panel').css('display') != 'none'){
                    $(this).next('.panel').css('display', 'none');
                  }
                  else {
                    $(this).next('.panel').css('display', 'block');
                  }
                });
}
</script>
