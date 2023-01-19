---

layout: full-width
title: OWASP Membership Information & Benefits
permalink: /membership/
maintenance: false
maintenance_message: Due to a required update to our systems, we are currently experiencing issues with our Membership portal, renewals, and joining. Thank you for your patience as we work to resolve the issues.

---

<style>
[v-cloak] {display: none}
.shared-header {
  width: 50%;
  display: inline;
  padding: 8px;
  border-left: 2px solid darkgray;
  border-top: 2px solid darkgray;
  border-right: 2px solid darkgray;
  border-radius: 4px;
  margin-right: 6px;
}

.unselected {
  background: lightgray;
}
</style>
{% if page.maintenance %}
<br><br><br>
{{ page.maintenance_message }}
<br><br><br>
{% else %}
{% raw %}
<div id="membership-app" style="margin: 0px;" v-cloak>
  <div class="col-sidebar">
    <div class="main-wrapper" style="padding: 0px;">
      <div>
      <!-- main membership form -->
      <div style='margin-top: 8px; margin-bottom: 8px;'><h1 class='shared-header'>Individual Membership</h1><h1 class='shared-header unselected'><a href="/supporters/">Corporate Membership</a></h1></div>
      <img src="/assets/images/web//members-header.png" alt="Attendees at a Global AppSec Conference">
      <p>One of many ways you can get involved in the OWASP Foundation is to become a member. It is through our global membership that we move forward on our mission to secure the web. We encourage and support diversity in AppSec and hope you will join us. <strong>Please note we also offer regional pricing to make OWASP accessible to everyone.</strong></p>
<!-- The member_benefits page is found at https://github.com/OWASP/owasp.github.io/blob/main/_includes/member_benefits.md-->
{% endraw %}
      {% include member_benefits.md %}
{% raw %}
      <!--<div class='alert'>Lifetime Memberships are now 10% off as part of the <a href="https://20thanniversary.owasp.org">OWASP 20th Anniversary Celebration</a></div>-->
      <p>Membership starts at $50 USD (or <a href="/membership?student=yes">$20 for students</a>) and, as noted above, there are discounts depending on your region.</p>
      <p>You can also <a href="/manage-membership">Manage your Membership</a> to provision an OWASP email address, check your renewal date or, for recurring donations and memberships, update billing details or cancel the recurring bill.</p>
      <p>Would your business like to become a <a href="/supporters">Corporate Member</a>? </p>
      <h2>Join or Renew Now</h2>
      <form class="form-container" v-on:submit.prevent="handleSubmit">
        <div class="error-text" style="font-size: 90%; margin-bottom: 16px" id="error-message" v-if="Object.keys(errors).length">
          Please correct the errors below before proceeding.
        </div>
        <div class="form-row" style="margin-bottom: 25px;">
          <div class="three-fourths">
            <select v-model="country">
              <option value="null">Country of Residence</option>
              <option v-for="item in countries" v-bind:value="item">
                {{ item.name }}
              </option>
            </select>
            <div class="error-text" v-if="errors.country">
              {{ errors.country[0] }}
            </div>
          </div>
          <div class="quarter">
            <input type="text" v-model="postal_code" aria-label="Postal Code"
            placeholder="Postal Code" />
            <div class="error-text" v-if="errors.postal_code">
              {{ errors.postal_code[0] }}
            </div>
          </div>
        </div>
        <div class="form-row" style="margin-bottom: 8px;" v-if="!free_leader">
          <div class="membership-option" v-for="membership in membershipOptions" v-on:click="updateMembership(membership.name, membership.discount)" v-bind:class="membership_type === membership.name ? 'selected' : ''">
            {{ membership.name }} {{ membership.amount }} {{membership.special}}
          </div>
        </div>
        <div class="error-text" v-if="errors.membership_type">
          {{ errors.membership_type[0] }}
        </div>
        <div style="margin-bottom: 35px; margin-top: 35px;">
	  <label class="checkbox-container" v-if="showAutoRenew">Set my Membership to Auto-renew
	    <input type="checkbox" v-model="auto_renew">
	    <span class="checkmark"></span>
	  </label>
	  <label class="checkbox-container">Join the OWASP Mailing List (See details below)
	    <input type="checkbox" v-model="mailing_list">
	    <span class="checkmark"></span>
	  </label>
    <label class="checkbox-container">I am requesting <a href="https://owasp.org/www-policy/operational/membership#complimentary-membership" target="_blank">Complimentary Membership for OWASP Leaders</a>
	    <input type="checkbox" v-model="free_leader">
	    <span class="checkmark"></span>
	  </label>
    <div class='error-text' v-if="errors.free_leader">
       {{ errors.free_leader[0] }}
       <br>Please <a href='https://contact.owasp.org/'>Contact Us</a> if you feel this was in error.
    </div>
    <label class="checkbox-container" v-if="free_leader">I agree to be bound by the <a href="https://owasp.org/www-policy/legal/leaders-commitment-agreement">Leader Agreement</a>
	    <input type="checkbox" v-model="free_leader_agreement">
	    <span class="checkmark"></span>
	  </label>
    <div class='error-text' v-if="errors.free_leader_agreement">
       {{ errors.free_leader_agreement[0] }}
    </div>
        </div>
        <div class="membership-fields">
          <h3>Your Information</h3>
	  <h4>If renewing, please use the same email address you used originally when joining</h4>
          <div>
            <input type="text" v-model="email" aria-label="Email Address"
            placeholder="Member Email Address" />
            <div class="error-text" v-if="errors.email">
              {{ errors.email[0] }}
            </div>
          </div>
          <div>
            <input type="text" v-model="email_confirm" aria-label="Confirm Email
            Address" placeholder="Confirm Member Email Address" />
            <div class="error-text" v-if="errors.email_confirm">
              {{ errors.email_confirm[0] }}
            </div>
          </div>
          <div v-if="student">
            <input type="text" v-model="university" aria-label="University" placeholder="University" />
            <div class="error-text" v-if="errors.university">
              {{ errors.university[0] }}
            </div>
          </div>
          <div v-else>
            <input type="text" v-model="company_name" aria-label="Company Name" placeholder="Company Name" />
            <div class="error-text" v-if="errors.company_name">
              {{ errors.company_name[0] }}
            </div>
          </div>
          <div>
            <input type="text" v-model="name_on_card" aria-label="Name" placeholder="Member Name" />
            <div class="error-text" v-if="errors.name_on_card">
              {{ errors.name_on_card[0] }}
            </div>
          </div>
        </div>
        <div class="submit-container">
          <button type="submit" class="membership-button" v-bind:disabled="loading"><div v-if="!loading">Submit</div><div class='spinner' v-if="loading"><div class='inner-spinner' v-if="loading"></div>
        </div></button>
        </div>        
      </form>
      <p class="legal-text">By submitting this form, you are consenting to receive communications from the OWASP Foundation concerning the status of your membership and agree to adhere to the OWASP Foundation <a href="/www-policy/operational/code-of-conduct">Code of Conduct</a>. Membership Dues are not prorated nor can they be cancelled once purchased. Discounted and <a href="/membership?student=yes">Student Memberships</a> are only offered to qualifying individuals. Fraudulent membership submissions will be revoked without notice for no refund. You can elect to receive marketing mails from us by also selecting "Join the OWASP Marketing Mail List." Marketing mails include information and special offers for upcoming conferences, meetings, and other opportunities offered to you. You can revoke your consent to receive Marketing Mail List emails at any time by using the Unsubscribe link found at the bottom of these emails.</p>
      <!-- end membership form -->
      </div>
      <aside class="sidebar" role="complementary">
        <!-- reserved for future use -->
      </aside>
    </div>
  </div>
</div>
{% endraw %}

<script src="https://js.stripe.com/v3"></script>
<script src="https://unpkg.com/vue@2/dist/vue.min.js"></script>
<script src="https://unpkg.com/axios/dist/axios.min.js"></script>

<script>
var stripe = Stripe('pk_live_mw0B2kiXQTFkD44liAEI03oT00S5AGfSV3');
window.addEventListener('load', function () {
  new Vue({
    el: '#membership-app',
    data: {
      loading: false,
      errors: {},
      countries: {{ site.data.countries | jsonify }},
      membership_type: null,
      membership_amount: null,
      membership_discount: null,
      country: null,
      postal_code: null,
      email: null,
      email_confirm: null,
      name_on_card: null,
      company_name: null,
      university: null,
      auto_renew: false,
      student: false,
      mailing_list: false,
      free_leader: false,
      free_leader_agreement: false,
    },
    created: function () {
      const queryParams = new URLSearchParams(window.location.search);
      if (queryParams.has('student')) {
        this.student = true
        this.membership_type = 'One Year';
        this.membership_discount = false;
        this.$forceUpdate();
      }
      if(queryParams.has('email')){
        this.email = queryParams.get('email')
        
      }
    },
    computed: {
      showAutoRenew: function () {
        return !this.student && this.membership_type == 'One Year'
      },
      membershipOptions: function () {
        
        if (!this.country || !this.country.hasOwnProperty('discount') ||
        this.country.discount == false) {
	  if (this.student) {
          return [
            { name: 'One Year', amount: '$20', discount: false }
          ];
        } else {
          return [
            { name: 'One Year', amount: '$50', discount: false },
            { name: 'Two Year', amount: '$95', discount: false },
            { name: 'Lifetime', amount: '$500', discount: false}
          ];
	  }
        } else {
	  if (this.student) {
          return [
            { name: 'One Year', amount: '$8', discount: true }
          ];
          }else{
          return [
            { name: 'One Year', amount: '$20', discount: true }, 
            { name: 'Two Year', amount: '$35', discount: true }, 
            { name: 'Lifetime', amount: '$200', discount: true} 
          ]
	  }
        }
      }
    },
    watch: {
      country: function (newCountry, oldCountry) {
        // if (this.student) {
        //   return;
        // }

        if (newCountry.discount) {
          //this.membership_type = 'One Year';
          this.membership_discount = true;
          this.$forceUpdate();
        } else if (oldCountry && oldCountry.discount) {
          this.membership_type = null;
          this.membership_discount = false;
          this.$forceUpdate();
        }
      }
    },
    methods: {
      handleSubmit: function () {
        
        if (this.free_leader){
          return this.handleLeaderSubmit();
        }

        this.loading = true;
        this.validateForm();
        
        if (Object.keys(this.errors).length > 0) {
          this.loading = false;
          //this works...why not in the axios post?
          this.$nextTick(function () {
            document.getElementById('error-message').scrollIntoView();
          })
        } else {
          const postData = {
            checkout_type: 'membership',
            membership_type: this.membership_type,
            discount: this.membership_discount,
            recurring: this.auto_renew,
            country: this.country,
            postal_code: this.postal_code,
            email: this.email,
            name: this.name_on_card,
            company: this.company_name,
            university: this.university,
            mailing_list: this.mailing_list,
            free_leader: this.free_leader,
            student: this.student,
            currency: 'usd'
          };
          axios.post('https://owaspadmin.azurewebsites.net/api/CreateCheckoutSession?code=ulMNYVfgzBytI1adat1lS6MQ3NabtwKE4IgCJ8yKuhvbFoQh6nOYaw==', postData)
            .then(function (response) {
              stripe.redirectToCheckout({
                sessionId: response.data.data.session_id
              }).then(function (result) {
                console.log(result.error.message)
              }); 
            })
            .catch(function (error) {
              vm.errors = error.response.data.errors
              vm.loading = false
              vm.$nextTick(function(){
                document.getElementById('error-message').scrollIntoView();
              })
            });
        }
      },
      handleLeaderSubmit: function() {
        this.loading = true;
        this.validateForm();
          // check the function call for free leader, if not leader, give error
        if (Object.keys(this.errors).length > 0) {
          this.loading = false;
          //this works...why not in the axios post?
          this.$nextTick(function () {
            document.getElementById('error-message').scrollIntoView();
          })
        } else {
          const postData = {
            checkout_type: 'membership',
            membership_type: 'complimentary',
            discount: this.membership_discount,
            recurring: this.auto_renew,
            country: this.country['name'],
            postal_code: this.postal_code,
            email: this.email,
            name: this.name_on_card,
            company: this.company_name,
            university: this.university,
            mailing_list: this.mailing_list,
            free_leader: this.free_leader,
            student: this.student,
            leader_agreement: this.free_leader_agreement,
            currency: 'usd'
          };
          let errors = {}
          // so instead of this...just create the membership? https://owaspadmin.azurewebsites.net/api/IsLeaderByEmail?code=yGSVCT1EaQHhLsVhbF6zEiOUninaB/jT4CIO9OyNdqg7lVmr8J4jLA==
          axios.post('https://owaspadmin.azurewebsites.net/api/CreateLeaderMembership?code=4ooIeXPupxNPTpIXRsPEiIDEhpeuTmr9wmsURjLHXCm3YFozQHfNwA==', postData)
            .then(response => {
              
              if(response.data.error){
                errors = [response.data.error]
                this.errors = errors
                if (response.data.error.indexOf('agreement') > 0)
                  errors.free_leader_agreement = [response.data.error];
                else
                  errors.free_leader = [response.data.error];
              }
              else{
                //success case?
                this.$nextTick(function () {
                    document.location.href = "/membership-success"
                  })
              }
              this.loading = false
              if (Object.keys(this.errors).length > 0) {
                this.loading = false;
                
                this.$nextTick(function () {
                  document.getElementById('error-message').scrollIntoView();
                })
              }
            })
            .catch(error => {
              errors = [error]
              errors.free_leader = [error]
              this.errors = errors
              this.loading = false
              if (Object.keys(this.errors).length > 0) {
                this.loading = false;
                
                this.$nextTick(function () {
                  document.getElementById('error-message').scrollIntoView();
                })
              }
            });
        }
      },
      updateMembership: function (name, discount) {
        this.membership_type = name;
        this.membership_discount = discount;
        this.$forceUpdate();
      },
      validateForm: function () {
        let errors = {};        

        if (!this.membership_type && !this.free_leader) {
          errors.membership_type = ['Please select a membership type.'];
        }

        if(this.free_leader && !this.free_leader_agreement){
          errors.free_leader_agreement = ['You must accept the leader agreement.']
        }

        if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(this.email)) {
          errors.email = ['Please enter a valid email address'];
        }

        if (this.email_confirm !== this.email) {
          errors.email_confirm = ['Both email addresses must match.'];
        }

        if(!this.name_on_card) {
          errors.name_on_card = ['Please enter you first and last name.'];
        }
        else {
          fname = this.name_on_card.substr(0, this.name_on_card.indexOf(' '));
          lname = this.name_on_card.substr(this.name_on_card.indexOf(' ') + 1);

          if (!fname || !lname) {
            errors.name_on_card = ['Please enter your first and last name.'];
          }
        }

        if (this.student && !this.university) {
          errors.university = ['Please enter your university name'];
        }

        if (!this.country) {
          errors.country = ['Please select your country.'];
        }

        if (!this.postal_code) {
          errors.postal_code = ['Please enter your postal code.'];
        }

        this.errors = errors;
      }
    }
  })
}, false)
</script>
{% endif %}
