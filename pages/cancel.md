---

layout: col-generic
title: Donate
permalink: /cancel

---


We are sorry to see that you had difficulty with the donation process.  Please try again.

<div>
  Returning to <a href="https://wwww2.owasp.org/">the main site</a> after <span id="countdown">10</span> seconds
</div>
<!-- JavaScript part -->
<script type="text/javascript">
    
    // Total seconds to wait
    var seconds = 10;
    
    function countdown() {
        seconds = seconds - 1;
        if (seconds < 0) {
            // Chnage your redirection link here
            window.location = "https://www2.owasp.org";
        } else {
            // Update remaining seconds
            document.getElementById("countdown").innerHTML = seconds;
            // Count down using javascript
            window.setTimeout("countdown()", 1000);
        }
    }
    
    // Run countdown function
    countdown();
    
</script>