---
title: OWASP Local Chapters
layout: col-sidebar
permalink: /chapters/
site_side: true
tags: chapters
---

<!-- rebuild 1 -->

<img src="/assets/images/web/chaper-wide.jpg" alt="Bay Area Chapter Meeting">

OWASP Local Chapters build community for application security professionals around the world. Our Local Chapter Meetings are **free and open** to anyone to attend so both members and non-members are always welcomed. Local meetings include:

- Training to improve your skills
- Talks relevant to your work
- Networking opportunities

Chapter pages on this site have general information and leader contact info. Local meeting RSVPs are handled through [https://meetup.com/pro/owasp](https://meetup.com/pro/owasp).


<div>
<label for='chapters-filter'>Filter List:</label>
<input type='text' id='chapters-filter'>
</div>

## Local Chapters by Region
{% assign regions = site.data.supported_regions %}
<ul>
    {% for region in regions %}
    <li><a href='#{{ region.region | remove: " " }}'>{{ region.region }}</a></li>
    {% endfor %}
</ul>

<a href="https://meetup.com/pro/owasp" target="_blank" rel="noopener"><button class="cta-button grey">Search using Map</button></a>


## Chapter Listing

<div class='chapters-list'>
    {% assign regions = site.data.supported_regions %}
    {% for region in regions %}
        {% assign rcount = 0 %}
        <div class="region">
            <h4><a name="{{ region.region | remove: " " }}"></a>{{ region.region }}</h4>
            <ul>
            {% for chapter in site.data.chapters %}
                {% if chapter.region == region.region and chapter.build != 'no pages'%}
                {% assign rcount = rcount | plus: 1 %}
                    <li><a href='{{ chapter.url }}'>{{ chapter.title }}</a></li>
                {% endif %}
            {% endfor %}
            </ul>
            Total: {{rcount}}
        </div>
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

<section id='leaders-list'>
<ul>
  {% assign group = '' %}
  {% for leader in allleaders %}
    {% if group != leader.group %}
      {% if group != '' %}
      </ul>
      {% endif %}
      {% assign group = leader.group %}
      {% assign leaders = site.data.leaders | where: 'group', leader.group %}
      {% capture leader_emails %}{% for leader in leaders %} {% assign email = leader.email | replace: 'mailto:','' | replace: '//', ''%}{{ email }}{% unless forloop.last %},{% endunless %}{% endfor %}{% endcapture %}
      <li><a href="{{leader.group_url}}">{{group}}</a><a href='mailto:{{leader_emails | strip}}' style='padding-left:1em;' title='Mail the leaders'><i class="fa fa-envelope" style='color:lightblue;'></i></a></li>
      <ul>
    {% endif %}
    <li><a href='mailto:{{ leader.email | replace: "mailto://", "mailto:" }}' target="_blank">{{ leader.name }}</a></li>
    {% if forloop.last %}
    </ul>
    {% endif %}
  {% endfor %}
</ul>
</section>

<script type='text/javascript'>
    var all = "{{ site.data.chapters | jsonify | replace: '"', '\"' | replace: '\\"', "'" }}";
    var chapters = JSON.parse(all);
    chapters = chapters.sort(function (a, b) {
      if(a.region > b.region) 
        return 1;
      else if(b.region > a.region)
        return -1;
      else
        return 0; 
    });
    alert(chapters);

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
            var filter = $('#chapters-filter').val();
            filter = filter.toLowerCase();
            var fleaders = []; 
            
              for(i = 0; i < leaders.length; i++){
                var group = leaders[i].group.toLowerCase();
                var email = leaders[i].email.toLowerCase();
                var name = leaders[i].name.toLowerCase();
                if(filter == '' || group.indexOf(filter) > -1 || email.indexOf(filter) > -1 || name.indexOf(filter) > -1)
                {
                  fleaders.push(leaders[i]);
                }
              }
            var html = "<ul>";
            var group = '';
            for(i = 0; i < fleaders.length; i++){
                email = fleaders[i].email;
                name = fleaders[i].name;
                if(group != fleaders[i].group)
                {
                  if(group != '')
                    html += "</ul>";

                  group = fleaders[i].group;
                  group_url = fleaders[i].group_url;
                  emails = getLeaderEmailsForGroup(fleaders, group);
                  html += "<li><a href='" + group_url + "'>";
                  html += group + "</a><a href='" + emails;
                  html += "' style='padding-left:1em;' title='Mail the leaders'><i class='fa fa-envelope' style='color:lightblue;'></i></a></li>";
                  html += '<ul>';
                }
                html += "<li><a href='mailto:" + email + "' target=\"_blank\">" + name + "</a></li>";
            }
            html += "</ul>";
            $('#leaders-list').html(html);
          }
      });
</script>
