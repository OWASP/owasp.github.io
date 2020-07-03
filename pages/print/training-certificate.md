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

<!--  parse query string  -->

<script type = "text/javascript">
  function getUrlParameter(name) {
      name = name.replace(/[\[]/, '\\[').replace(/[\]]/, '\\]');
      var regex = new RegExp('[\\?&]' + name + '=([^&#]*)');
      var results = regex.exec(location.search);
      return results === null ? '' : decodeURIComponent(results[1].replace(/\+/g, ' '));
  };
  
  getUrlParameter('name'); // "Billy Bob Smith"
  getUrlParameter('event'); // "AppSec Days"
  getUrlParameter('class'); // "Defensive coding in JavaScript"
  getUrlParameter('hours'); // "8"
  getUrlParameter('date'); // "June 24, 2020"
  getUrlParameter('price'); // "$495"

</script>


<!--  page to print  -->

<div class="certificate-header">
</div>

<div class="content">

  <img src="/assets/images/logo.png" height="72"> 
  <p style="font-size:36px">OWASP<sup>&reg;</sup> Foundation</p>
  <p style="font-size:28px">Training Certificate</p> 
  <p style="font-size:42px"><strong>{{ name }}Billy Bob Smith</strong></p>
  <p style="font-size:36px">{{ class }}Training: Defensive coding in JavaScript</p>
  <p style="font-size:18px">Completed on {{ date }}June 24, 2020 for a total of {{ hours }}8 Continuing Education Credits</p>

</div>

<div class="certificate-footer">
    <p class="disclaimer">
    Printed {{ "now" | date: "%B %-d, %Y" }}. Open Web Application Security Project and OWASP are registered trademarks and Global AppSec, AppSec Days, AppSec California, SnowFROC, LASCON, and the OWASP logo are trademarks of the OWASP Foundation, Inc.  
    </p>
</div>
