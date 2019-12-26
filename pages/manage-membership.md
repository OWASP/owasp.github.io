---

layout: full-width
title: Manage your Information
permalink: /manage-membership

---

<style>
[v-cloak] {display: none}

#manage-membership-app input:focus, #manage-membership-app select:focus {
  outline: none;
}

.form-container {
  margin: 40px 0px;
  max-width: 100%;
}

.error-text {
  color: #ff0000;
  font-size: 75%;
  margin-top: 4px !important;
}

.form-container input {
  width: 100%;
  border: 1px solid #000000;
  padding: 8px;
}

.submit-button {
  border: 0;
  padding: 16px;
  font-weight: bold;
  color: #ffffff;
  background-color: #233e81;
  text-transform: uppercase;
  font-size: 110%;
}

.danger-button {
  background-color: #dc3545;
}

@media (min-width: 768px) {
  .form-container {
    max-width: 70%;
  }
}
</style>

{% raw %}
<div id="manage-membership-app" style="margin: 0px;" v-cloak>

  <div class="col-sidebar">
    <div class="main-wrapper" style="padding: 0px;">
      <div>

      <h1>Manage Your Membership</h1>

      <div v-if="state === 'unsubmitted'">
        <p>If you have an existing OWASP membership or recurring gift, enter your address below and you will receive an email response that includes a URL which you can visit to update your billing information.</p>
        <form v-on:submit.prevent="handleSubmit" class="form-container">
        <div class="error-text" style="font-size: 90%; margin-bottom: 16px" id="error-message" v-if="Object.keys(errors).length">
          Please correct the errors below before proceeding.
        </div>
        <div style="margin-bottom: 18px;">
        <input type="text" v-model="email" v-on:input="updateErrors" aria-label="Email Address"
        placeholder="Email Address" />
        <div class="error-text" v-if="errors.email">
        {{ errors.email[0] }}
        </div>
        </div>
        <div>
        <button type="submit" class="submit-button" v-bind:disabled="loading">Request Account Information</button>
        </div>
        </form>
      </div>
      <div v-else-if="state === 'submitted'">
        <p>Thanks! We just sent you an email with instructions for how to update
        your membership or payment information. The internet is fast but sometimes our bots are slow. Please wait 5-10 minutes for your email. If you don't receive one, please check your SPAM folder as well. If all else fails, you likely used an email address we didn't find in our system.</p>
      </div>
      <div style="display: flex;" v-else-if="state === 'redirecting'">
        <div style="margin-right: 18px;">
          <button v-on:click="redirectToStripe" class="submit-button" v-bind:disabled="loading">Update Payment Information</button>
        </div>
        <div>
        <button v-on:click="doCancellation" class="submit-button danger-button" v-bind:disabled="loadingCancellation">{{ pendingCancellation ? 'Are you sure?' : 'Cancel Membership' }}</button>
        </div>
      </div>
      <div v-else-if="state === 'cancelled'">
      <p>We're sorry to see you go! Your OWASP information has been modified. You will remain a member until the end of your current billing period.</p>
      </div>

      </div>
      <aside class="sidebar" role="complementary">
        <!-- reserved for future use -->
      </aside>
    </div>
  </div>

</div>
{% endraw %}

<script src="https://js.stripe.com/v3"></script>
<script src="https://unpkg.com/vue"></script>
<script src="https://unpkg.com/axios/dist/axios.min.js"></script>

<script>
var stripe = Stripe('pk_test_u4OyMFMbz6tp9sit2bjdHRnT00bac5mrL2');
window.addEventListener('load', function () {
  new Vue({
    el: '#manage-membership-app',
    data: {
      email: null,
      errors: {},
      loading: false,
      pendingCancellation: false,
      loadingCancellation: false,
      state: 'unsubmitted'
    },
    created: function () {
      const queryParams = new URLSearchParams(window.location.search);
      if (queryParams.has('token')) {
        this.state = 'redirecting';
        this.checkoutSessionId = queryParams.get('token');
      }
    },
    methods: {
      handleSubmit: function () {
        this.loading = true;
        this.validateForm();

        if (Object.keys(this.errors).length > 0) {
          this.loading = false;
          this.$nextTick(function () {
            document.getElementById('error-message').scrollIntoView();
          });
        } else {
          let vm = this;
          const postData = {
            checkout_type: 'manage_membership',
            email: vm.email
          };
          axios.post('https://owaspadmin.azurewebsites.net/api/CreateCheckoutSession?code=ulMNYVfgzBytI1adat1lS6MQ3NabtwKE4IgCJ8yKuhvbFoQh6nOYaw==', postData)
            .then(function (response) {
              vm.state = 'submitted';
            })
            .catch(function (error) {
              vm.errors = error.response.data.errors
              vm.$nextTick(function () {
                document.getElementById('error-message').scrollIntoView();
              })
            })
            .finally(function () {
              vm.loading = false
            })
        }
      },
      validateForm: function () {
        let errors = {};
        if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(this.email)) {
          errors.email = ['Please enter a valid email address'];
        }
        this.errors = errors;
      },
      updateErrors: function () {
        if (Object.keys(this.errors).length > 0) {
          this.validateForm();
        }
      },
      redirectToStripe: function (sessionId) {
        stripe.redirectToCheckout({
          sessionId: this.checkoutSessionId
        }).then(function (result) {

        }); 
      },
      doCancellation: function () {
        if (this.pendingCancellation) {
          let vm = this;
          const postData = {
            token: this.checkoutSessionId
          };
          vm.loadingCancellation = true;
          axios.post('https://owaspadmin.azurewebsites.net/api/CancelSubscription?code=Wo2wqKKpOMZP0LycmMGWLl3z8wGqK0BoIPRL/3At9W31ZnHZSRn8xw==', postData)
            .then(function (response) {
              vm.state = 'cancelled';
            })
            .catch(function (error) {

            })
            .finally(function () {
              vm.loadingCancellation = false
            })
        } else {
          this.pendingCancellation = true;
        }
      }
    }
  })
}, false)
</script>
