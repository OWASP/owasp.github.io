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
  <section id="invoice"> 
  
  </section>

</div>

<div class="certificate-footer">
    <p class="disclaimer">
    Printed {{ "now" | date: "%B %-d, %Y" }}. Open Web Application Security Project and OWASP are registered trademarks and Global AppSec, AppSec Days, AppSec California, SnowFROC, LASCON, and the OWASP logo are trademarks of the OWASP Foundation, Inc.  
    </p>
</div>


<!--  parse query string  -->
<script type = "text/javascript">
// example url: https://owasp.org/pages/print/invoice?name=Mike%20McCamon&company=Apple&payment=pm_1Gx6eCAqEqYTAl67mjPkeFLQ&event=Virtual%20AppSect&class=Defending%20Kubernetes&hours=8&date=June%2020,%202020&price=$495%20USD

  function getUrlParameter(name) {
      name = name.replace(/[\[]/, '\\[').replace(/[\]]/, '\\]');
      var regex = new RegExp('[\\?&]' + name + '=([^&#]*)');
      var results = regex.exec(location.search);
      return results === null ? '' : decodeURIComponent(results[1].replace(/\+/g, ' '));
  }
  
  jname = getUrlParameter('name'); // "Billy Bob Smith"
  jcompany = getUrlParameter('company'); // "Apple"
  jevent = getUrlParameter('event'); // "AppSec Days"
  jtraining = getUrlParameter('class'); // "Defensive coding in JavaScript"
  jpayment = getUrlParameter('payment'); // "pm_1Gx6eCAqEqYTAl67mjPkeFLQ"
  jhours = getUrlParameter('hours'); // "8"
  jdate = getUrlParameter('date'); // "June 24, 2020"
  jprice = getUrlParameter('price'); // "$495"
  
  hstr = "<p style='font-size:24px;'>OWASP<sup>&reg;</sup> Foundation Training Invoice</p>";
  hstr += "<p style='font-size:18px;'>401 Edgewater Place, Suite 600<br>Wakefield, MA 01880</p>";
  hstr += "<hr>";
  hstr += "<p style='font-size:18px;'>Invoice/Payment ID: " + jpayment + "</p>";
  hstr += "<p style='font-size:18px;'>Payment date " + jdate + "</p>";
  hstr += "<hr>";
  hstr += "<p style='font-size:18px;'><strong>Bill to:</strong><br>" + jname + "<br>" + jcompany + "</p>";
  hstr += "<p style='font-size:18px;'><strong>Description and Amount</strong><br>" + jevent + ", " + jtraining + " - " + jprice + "</p>";
  tsec = document.getElementById("invoice");
  tsec.innerHTML = hstr;
</script>
<!--  page to print  -->
