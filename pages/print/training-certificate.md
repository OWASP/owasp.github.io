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

  .repeating-linear {
  margin:auto;
  max-width: 60%;
  color: grey;
  border: 60px solid grey;
  border-image: url(/assets/images/fancy1-black.jpg) 30% round;
  }

  .content {
    color: black;
  }

  @media print { 
			.noprint { 
				visibility: hidden; 
			}

      .repeating-linear {
        max-width: 100%;
      } 
  }
</style>

<div class='repeating-linear'>
  <div class="content">
    <div style='line-height:72px;text-align:center;margin-bottom:40px;'>
      <img src="/assets/images/logo.png" height="72px"><div style='display:block; height:72px; margin-left: 12px; font-weight:bold; font-size: 2em; vertical-align:middle; line-height:normal;'>Training Certificate of Completion</div>
    </div>
    <section id="training"> 
    </section>
  </div>
  <div class="certificate-footer noprint">
      <p class="disclaimer">
      Open Web Application Security Project and OWASP are registered trademarks and Global AppSec, AppSec Days, AppSec California, SnowFROC, LASCON, and the OWASP logo are trademarks of the OWASP Foundation, Inc.  
      </p>
  </div>
</div>

<!--  parse query string  -->
<script type = "text/javascript">
// example url: https://owasp.org/pages/print/training-certificate?name=Mike%20McCamon&event=Virtual%20AppSect&class=Defending%20Kubernetes&hours=8&date=June%2020,%202020


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
  jsku = getUrlParameter('sku'); // sku_HOts6ZxZnmJERL
  // hstr = "<p style='font-size:36px;'>OWASP<sup>&reg;</sup> Foundation Training Certificate</p>";
  hstr = "<p style='font-size:24px;margin-left: 8px;'><span style='font-weight:bold;margin-right:8px;'>Course Title:</span><span style='font-style:italic;'>" + jevent + ", " + jtraining + "</span></p>";
  hstr += "<p style='font-size:24px;margin-left: 8px;margin-right:8px;'><label style='margin-right:8px;font-weight:bold;'>Presented to:</label><span style='text-decoration:underline;'>" + jname + "</span></p>";
  hstr += "<p style='font-size:18px'>Completed on " + jdate + " for a total of " + jhours + " hours of Continuing Education Credits</p>";
  hstr += "<p style='font-size:18px'>Course ID:</span><span>" + jsku + "</p>";
  
  tsec = document.getElementById("training");
  tsec.innerHTML = hstr;
</script>
<!--  page to print  -->
