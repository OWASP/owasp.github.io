---

---


<style>
  .certificate-header {
    position: fixed;
    top: 0;
  }
  .certificate-footer {
    position: fixed;
    bottom: 0;
  }
</style>


<div class="certificate-header">
</div>

<div class="content">

  <img src="/assets/images/logo.png" height="72">
  <section id="training"> 
  
  </section>

</div>

<div class="certificate-footer">
    <p class="disclaimer">
    Printed {{ "now" | date: "%B %-d, %Y" }}. Open Web Application Security Project and OWASP are registered trademarks and Global AppSec, AppSec Days, AppSec California, SnowFROC, LASCON, and the OWASP logo are trademarks of the OWASP Foundation, Inc.  
    </p>
</div>


<!--  parse query string  -->
<script type = "text/javascript">
// example url: https://owasp.org/pages/print/training-certificate?name=Mike%20McCamon&event=Virtual%20AppSect&class=Defending%20Kubernetes&hours=8&date=10/10/2020


  function getUrlParameter(name) {
      name = name.replace(/[\[]/, '\\[').replace(/[\]]/, '\\]');
      var regex = new RegExp('[\\?&]' + name + '=([^&#]*)');
      var results = regex.exec(location.search);
      return results === null ? '' : decodeURIComponent(results[1].replace(/\+/g, ' '));
  };
  
  jname = getUrlParameter('name'); // "Billy Bob Smith"
  jevent = getUrlParameter('event'); // "AppSec Days"
  jtraining = getUrlParameter('class'); // "Defensive coding in JavaScript"
  jhours = getUrlParameter('hours'); // "8"
  jdate = getUrlParameter('date'); // "June 24, 2020"
  jprice = getUrlParameter('price'); // "$495"
  hstr = "<p style='font-size:36px;'>OWASP<sup>&reg;</sup> Foundation Training Certificate</p>";
  hstr += "<p style='font-size:42px'><strong>" + jname + "</strong></p>";
  hstr += "<p style='font-size:36px'>" + jtraining + "</p>";
  hstr += "<p style='font-size:18px'>Completed on " + jdate + " for a total of " + jhours + " Continuing Education Credits</p>";
  tsec = document.getElementById("training");
  tsec.innerHTML = hstr;
</script>
<!--  page to print  -->
