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
  getUrlParameter('class'); // "Training: Defensive coding in JavaScript"
  getUrlParameter('hours'); // "8"
  getUrlParameter('date'); // "June 24, 2020"
  getUrlParameter('price'); // "$495"

</script>


<!--  page to print  -->

<div class="certificate-header">
</div>

<div class="content">

  <img src="/assets/images/logo.png" height="200">
  
  <h2>OWASP<sup>&reg;</sup> Foundation</h2>
  
  <h3>Training Certificate</h3>
  
  <h4>{{ name }}</h4>
  {{ class }}
  
  Completed on {{ date }} for a total of {{ hours }} of Continuing Education Credits

</div>

<div class="certificate-footer">
    <p class="disclaimer">
    Printed {{ "now" | date: "%Y" }}. Open Web Application Security Project and OWASP are registered trademarks and Global AppSec, AppSec Days, AppSec California, SnowFROC, LASCON, and the OWASP logo are trademarks of the OWASP Foundation, Inc.  
    </p>
</div>
