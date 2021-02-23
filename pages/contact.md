---

layout: col-generic
title: Contact Us
permalink: /contact/

---

![Attendees at a Global AppSec Conference](/assets/images/web/about_header.png)

Most answers you might have about the OWASP Foundation can be found by searching this website. Another path to find information is to visit our [sitemap](/sitemap). The most common questions can be answered through the links below.

### Frequently Asked Questions

- How do I [Renew](/membership)  my OWASP Membership or [Manage Recurring](/manage-membership) Memberships?
- Where do I update my [Recurring Donor Billing](/manage-membership) information?
- How can Corporations [Sponsorships or Support](https://owasporg.atlassian.net/servicedesk/customer/portal/7/group/18/create/72) the OWASP Foundation?
- [Project](/projects) leader contact info is listed on each Projects page under Leaders
- Local [Chapter](/chapters) Leaders are listed on a Chapters' respective page
- Who do I contact for [Partnership Marketing](https://owasporg.atlassian.net/servicedesk/customer/portal/7/group/19/create/83) opportunities?

<a href="https://owasporg.atlassian.net/servicedesk/customer/portal/7/create/72" target="_blank" rel="noopener"><button class="cta-button dark">Contact Us</button></a>

<h4>Enter your email to join our Slack community</h4>
<div id='div-slack-join' style='text-align:left;align-controls:center;padding: 8px;'>
    <label for='emailaddr'>Email Address</label><br>
    <input style='line-height: 24px;margin-bottom:8px;' id='emailaddr' type='email'><br>
    <button class="cta-button dark" id="btn-join-slack">Join</button>
</div>
<div id='div-slack-result' style="display:hidden;font-weight:bold;margin: 24px;">
</div>

Our global address for general correspondence and faxes can be sent to our physical office address, at: 

```
OWASP Foundation
1200-C Agora Drive, #232
Bel Air, MD 21014
+1 951-692-7703 (phone)
+1 443-283-4021 (fax)
EIN #20-0963503
```

The European legal address is:

```
OWASP Europe VZW
Leinstraat 104A
B-9660 Opbrakel
Belgium
```


<script type="text/javascript">
    $(function(){
        $('#btn-join-slack').click(function(){
            var email = $('#emailaddr').val();
            $.ajax({
                type: "POST",
                url: "https://owaspadmin.azurewebsites.net/api/owasp_slack_add_user?code=aaanp3ICdjlaVHHoAnmO06EiDh9dgrCZfkjdTeoOQLVvdesivNWUjA==&email=" + email,
                dataType: "json",
                success: function (result, status, xhr) {
                   if(result['ok']){
                    $("#div-slack-join").hide();
                    $("#div-slack-result").text("Thanks for joining!  Be on the lookout for an email with more information.");
                    $("#div-slack-result").show();
                   }else {
                    $("#div-slack-join").hide();
                    $("#div-slack-result").text("Oops!  Looks like something went wrong or you are already signed up.");
                    $("#div-slack-result").show();    
                   }
                },
                error: function (xhr, status, error) {
                   $("#div-slack-join").hide();
                   $("#div-slack-result").text("Oops!  Looks like something went wrong or you are already signed up.");
                   $("#div-slack-result").show();
                }
            });
        });
    });
</script>