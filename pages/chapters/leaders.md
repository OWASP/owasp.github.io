---

title: Chapter Leaders
layout: col-generic
permalink: /chapters/leaders/

---

{% assign allleaders = site.data.leaders | where: 'group-type','chapter' %}
<p>
<div>
<label for='leaders-filter'>Filter List:</label>
<input type='text' id='leaders-filter'>
</div>
<section id='leaders-list'>
<ul>
  {% for leader in allleaders %}
  <li><a href='{{ leader.email | replace: "mailto://", "mailto:" }}' target="_blank">{{ leader.name }}</a> : {{ leader.group }}</li>
  {% endfor %}
</ul>
</section>

<script type='text/javascript'>
    var all = "{{ allleaders | jsonify | replace: '"', '\"' }}";
    var leaders = JSON.parse(all);
     
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
            if(group.indexOf(filter) > -1 || email.indexOf(filter) > -1 || name.indexOf(filter) > -1)
            {
               fleaders.push(leaders[i]);
            }
          }
         var html = "<ul>";
         for(i = 0; i < fleaders.length; i++){
            html += "<li><a href='" + fleaders[i].email + "' target=\"_blank\">" + fleaders[i].name + "</a>:" + fleaders[i].group + "</li>";
         }
         html += "</ul>";
         $('#leaders-list').html(html);
       }
   });
</script>