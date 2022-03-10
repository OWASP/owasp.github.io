---

title: Callback Auth For MU Temp
layout: full-width
permalink: /mu_auth/

---

### Temporary Page for Callback

<div id='at'>
</div>


<script text="text/javascript">
    $(function() {
        $('#at').html(getParam('access_token'))
    });

    function getParam (name) {
        name = RegExp ('[?&]' + name.replace (/([[\]])/, '\\$1') + '=([^&#]*)');
        return (window.location.href.match (name) || ['', ''])[1];
    }
</script>