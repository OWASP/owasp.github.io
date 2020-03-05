---

title: Project Leaders
layout: col-sidebar

---

{% assign allleaders = site.data.leaders | where: 'group-type','project' %}
<label for='leaders-filter'>Filter List</label><input type='text' id='leaders-filter'></input>
<section id='leaders-list'>
  {% for leader in allleaders %}
  {{ leader.name }} : {{ leader.group }}
  {% endfor %}
</section>

<script type='text/javascript'>
  var leaders = {{ allleaders }};
  
 $(function() {
    $("#leaders-filter").keyup(function(e) {
     var code = e.keyCode ? e.keyCode : e.which;
     if (code == 13) {  // Enter keycode
        alert('filter it');
       }
   });
 });
</script>
