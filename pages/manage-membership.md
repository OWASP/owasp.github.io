---

layout: full-width
title: Manage Your Information
permalink: /manage-membership/

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

input[type='radio'] {
  margin-right: 16px;
  margin-top: 8px;
  margin-bottom: 8px;
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

      <h1>Manage Your Information</h1>

      <div v-if="state === 'unsubmitted'">
        <p>If you have an existing OWASP membership or recurring gift, enter your address (case sensitive) below and you will receive an email response that includes an URL which you can visit to update your billing information.</p>
        <form v-on:submit.prevent="handleSubmit" class="form-container">
        <div class="error-text" style="font-size: 90%; margin-bottom: 16px" id="error-message" v-if="Object.keys(errors).length">
          Please correct the errors below before proceeding.
        </div>
        <div style="margin-bottom: 18px;">
        <input type="text" v-model="email" v-on:input="updateErrors" aria-label="Email Address"
        placeholder="Email Address (case sensitive)" />
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
      <div style="display: flex;" v-else-if="state === 'hastoken'">
        <div v-if="loadingUserData">
          <h2>Loading Billing Information...</h2>
        </div>
        <div v-else>
          <div v-if="userData.membership" style="margin-bottom: 20px;">
            <div>
              <strong>Membership Type:</strong> {{ userData.membership.membership_name }}
            </div>
            <div v-if="userData.membership.membership_end">
              <strong>Membership {{ userData.membership.membership_recurring ? 'Automatically Renews On' : 'Ends On' }}:</strong> {{ userData.membership.membership_end }}
            </div>
          </div>
          <div v-if="memberships.length > 0" style="margin-bottom: 40px;">
            <h3>Manage Membership</h3>
            <div v-for="membership in memberships">
              <div><strong>{{ membership.subscription_name }}</strong></div>
              <div>{{ membership.card.brand }} ending in {{ membership.card.last_4 }}</div>
              <div>Next Billing Date: {{ membership.next_billing_date }}</div>
              <div style="margin-right: 18px; display: inline-block;">
                <button class="submit-button" v-on:click="redirectToStripe(membership.checkout_session)">Update Payment Information</button>
              </div>
              <div style="display: inline-block;">
                <button class="submit-button danger-button" v-on:click="doCancellation(membership.checkout_session)">{{ pendingCancellation === membership.checkout_session ? 'Are you sure?' : 'Cancel Recurring' }}</button>
              </div>
            </div>
          </div>
          <div v-if="donations.length > 0">
            <h3>Manage Recurring Donations</h3>
            <div v-for="donation in donations">
              <div><strong>{{ donation.subscription_name }}</strong></div>
              <div>{{ donation.card.brand }} ending in {{ donation.card.last_4 }}</div>
              <div>Next Billing Date: {{ donation.next_billing_date }}</div>
              <div style="margin-right: 18px; display: inline-block;">
                <button class="submit-button" v-on:click="redirectToStripe(donation.checkout_session)">Update Payment Information</button>
              </div>
              <div style="display: inline-block;">
                <button class="submit-button danger-button" v-on:click="doCancellation(donation.checkout_session)">{{ pendingCancellation === donation.checkout_session ? 'Are you sure?' : 'Cancel Recurring' }}</button>
              </div>
            </div>
          </div>
          <div v-if="provision_email_message == true">
               Your chosen email was created.  Please check your email address on file for a link to set your password.
          </div>
          <div id='email-section' v-if="userData.emaillist.length > 0">
            <hr>
            <h3>Provision Your OWASP Email</h3>
            <div v-if="userData.emaillist.length > 1">
              Choose one from the list below:<br>
              (If you already have an OWASP email, please do not provision another)
              <hr>
            </div>
            <div v-for="error in errors">
              <label class='error-text' id='provision-error'>{{error[0]}}</label>
            </div>
            <div v-for="email in userData.emaillist">
              <div style="display: inline-block;">
                <input type='radio' id='chosen_email' v-model='chosen_email' value='email'>&nbsp;&nbsp;{{email}}
              </div>
              
            </div>
            <div style='margin-top: 20px;'>
              <button class="submit-button" v-on:click="redirectToAzure()">Provision</button>
            </div>
          </div>
        </div>
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
<script src="https://cdnjs.cloudflare.com/ajax/libs/lodash.js/4.17.15/lodash.min.js"></script>

<script>
var stripe = Stripe('pk_live_mw0B2kiXQTFkD44liAEI03oT00S5AGfSV3');
window.addEventListener('load', function () {
  new Vue({
    el: '#manage-membership-app',
    data: {
      email: null,
      errors: {},
      loading: false,
      token: null,
      state: 'unsubmitted',
      userData: {
        subscriptions: [],
        emaillist: []
      },
      loadingUserData: true,
      pendingCancellation: null,
      chosen_email: '',
      provision_email_message: false
    },
    created: function () {
      const queryParams = new URLSearchParams(window.location.search);
      if (queryParams.has('token')) {
        this.token = queryParams.get('token');
        this.state = 'hastoken';
        this.getMemberInfo();
      }
    },
    computed: {
      memberships: function () {
        return _.filter(_.get(this.userData, 'subscriptions', []), { type: 'membership' });
      },
      donations: function () {
        return _.filter(_.get(this.userData, 'subscriptions', []), { type: 'donation' });
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
      getMemberInfo: function () {
        let vm = this;
        const postData = {
          token: this.token,
          action: 'info'
        };
        axios.post('https://owaspadmin.azurewebsites.net/api/billingmanagement?code=WDLIYfCkkBzaaanneE6Yzr3mld/GNnDIHVIoUo0XPvLae3AU2lfMAA==', postData)
          .then(function (response) {
            vm.userData = response.data.data;
            vm.loadingUserData = false;
          });
      },
      redirectToAzure: function () {
        let vm = this;
        if(vm.chosen_email == '')
        {
          let errors = {};
          errors.chosen_email = ['Please choose an email address.'];
          this.errors = errors;
          vm.$nextTick(function () {
                document.getElementById('provision-error').scrollIntoView();
              })
          return;
        }
        const postData = {
          token: this.token,
          email: vm.chosen_email
        };
        
        
        axios.post('https://owaspadmin.azurewebsites.net/api/provisionemail?code=KpGlIqooyYW3GYEHuYTYzRmwSiVbeGQ4xRRarY7UWhBLwoRASFVn3g==', postData)
          .then(function (response) {
                vm.userData.emaillist = []
                vm.provision_email_message = true
          }).catch(function (error) {
              vm.errors = error
            });
      },
      redirectToStripe: function (sessionId) {
        stripe.redirectToCheckout({
          sessionId: sessionId
        }).then(function (result) {

        }); 
      },
      doCancellation: function (sessionId) {
        if (this.pendingCancellation && this.pendingCancellation === sessionId) {
          let vm = this;
          const postData = {
            token: sessionId
          };
          axios.post('https://owaspadmin.azurewebsites.net/api/CancelSubscription?code=Wo2wqKKpOMZP0LycmMGWLl3z8wGqK0BoIPRL/3At9W31ZnHZSRn8xw==', postData)
            .then(function (response) {
              vm.loadingUserData = true;
              vm.getMemberInfo();
            }).finally(function () {
              vm.pendingCancellation = null;
            })
        } else {
          this.pendingCancellation = sessionId;
        }
      },
    }
  })
}, false)
</script>

Having membership problems? <a href="https://owasporg.atlassian.net/servicedesk/customer/portal/7/group/18/create/72" target="_blank" rel="noopener">Submit a Ticket</a>.
