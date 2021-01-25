---

title: Project Leaders
layout: col-sidebar
permalink: /projects/leaders/

---

{% assign allleaders = site.data.leaders | where: 'group-type','project' | order: 'group' | sort: 'group' %}
<p>
<div>
<label for='leaders-filter'>Filter List:</label>
<input type='text' id='leaders-filter'>
</div>
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
      {% capture leader_emails %}{% for leader in leaders %} {% assign email = leader.email | replace: 'mailto:','' | replace: '//', '' | replace: '\\', ''%}{{ email }}{% unless forloop.last %},{% endunless %}{% endfor %}{% endcapture %}
      <li><a href="{{leader.group_url}}">{{group}}</a><a href='mailto:{{leader_emails | strip}}' style='padding-left:1em;' title='Mail the leaders'><i class="fa fa-envelope" style='color:lightblue;'></i></a></li>
      <ul>
    {% endif %}
    <li><a href='{{ leader.email | replace: "mailto://", "mailto:" }}' target="_blank">{{ leader.name }}</a></li>
    {% if forloop.last %}
    </ul>
    {% endif %}
  {% endfor %}
</ul>
</section>

<script type='text/javascript'>
    var all = "{{ allleaders | jsonify | replace: '"', '\"' }}";
    var leaders = JSON.parse(all);
    leaders = leaders.sort(function (a, b) {
      if(a.group > b.group) 
        return 1;
      else if(b.group > a.group)
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
            emails += inleaders[x].email.replace('mailto://','').replace('mailto:\\','').replace('mailto:','');
            emails += ",";
          }
        }
        emails = emails.substring(0, emails.length - 1);
        return emails;
    }

    $("#leaders-filter").keyup(function(e) {
     var code = e.keyCode ? e.keyCode : e.which;
     
     if (code == 13) {  // Enter keycode
         var filter = $('#leaders-filter').val();
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
