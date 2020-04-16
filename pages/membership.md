---

layout: full-width
title: OWASP Membership Information & Benefits
permalink: /membership/

---

<style>
[v-cloak] {display: none}

#membership-app input:focus, #membership-app select:focus {
  outline: none;
}

.legal-text {
  font-size: 75%;
  color: #808080;
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

.form-container input, .form-container select {
  width: 100%;
  border: 1px solid #000000;
  padding: 8px;
}

.form-container select {
  -webkit-appearance: none;
  -moz-appearance: none;
  appearance: none;
  background-color: #ffffff;
  border-radius: 0px;
  font-size: 18px;
  padding: 9px;
}

.form-row {
  margin-bottom: 20px;
}

.membership-option {
  text-align: center;
  background-color: #D3D3D3;
  color: #000000;
  padding: 20px;
  font-weight: bold;
  cursor: pointer;
}

.membership-option.selected {
  background-color: #233e81;
  color: #ffffff;
}

.checkbox-container {
  display: block;
  position: relative;
  padding-left: 35px;
  margin-bottom: 12px;
  cursor: pointer;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

.checkbox-container input {
  position: absolute;
  opacity: 0;
  cursor: pointer;
  height: 0;
  width: 0;
}

.checkbox-container .checkmark {
  position: absolute;
  top: 0;
  left: 0;
  height: 25px;
  width: 25px;
  background-color: #eee;
}

.checkbox-container:hover input ~ .checkmark {
  background-color: #ccc;
}

.checkbox-container input:checked ~ .checkmark {
  background-color: #233e81;
}

.checkbox-container .checkmark:after {
  content: "";
  position: absolute;
  display: none;
}

.checkbox-container input:checked ~ .checkmark:after {
  display: block;
}

.checkbox-container .checkmark:after {
  left: 9px;
  top: 5px;
  width: 5px;
  height: 10px;
  border: solid white;
  border-width: 0 3px 3px 0;
  -webkit-transform: rotate(45deg);
  -ms-transform: rotate(45deg);
  transform: rotate(45deg);
}

.membership-fields {
  margin-bottom: 40px;
}

.membership-fields div {
  margin: 14px 0px;
}

.membership-button {
  border: 0;
  padding: 16px;
  font-weight: bold;
  color: #ffffff;
  background-color: #233e81;
  text-transform: uppercase;
  font-size: 110%;
}

@media (min-width: 768px) {
  .form-container {
    max-width: 70%;
  }

  .form-row {
    display: flex;
  }

  .form-row div:not(:last-child) {
    margin-right: 10px;
  }

  .membership-option {
    flex: 1;
    flex-basis: 0;
  }

  .quarter {
    flex: 1;
    flex-basis: 25%;
  }

  .three-fourths {
    flex: 1;
    flex-basis: 75%;
  }
}
</style>

{% raw %}
<div id="membership-app" style="margin: 0px;" v-cloak>

  <div class="col-sidebar">
    <div class="main-wrapper" style="padding: 0px;">
      <div>

      <!-- main membership form -->

      <h1>Individual Membership</h1>
      <img src="/assets/images/web//members-header.png" alt="Attendees at a Global AppSec Conference">

      <p>One of many ways you can get involved in the OWASP Foundation is to become a member. It is through our global membership that we move forward on our mission to secure the web. We encourage and support diversity in AppSec and hope you will join us. Please note we also offer regional pricing to make OWASP accessible to everyone. There are many benefits to membership including:</p>
      <ul> 
      	<li>Ongoing Support of our work</li>
	<li>Discounted Conference Fees</li>
	<li>Corporate owasp.org email address</li>
	<li>Priority access to Travel Grants</li>
	<li>And many others...</li>
	
	<li> OWASP emails have a standard format firstname.lastname@owasp.org; email addresses are only valid during membership and will be suspended 30 days after last day of membership if not renewed.</li>
      </ul>
      <p>You can <a href="/manage-membership">Manage your Membership</a> to check your renewal date or update billing details or cancel a recurring donation.</p>
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
        <div class="form-row" style="margin-bottom: 8px;">
          <div class="membership-option" v-for="membership in membershipOptions" v-on:click="updateMembership(membership.name, membership.discount)" v-bind:class="membership_type === membership.name ? 'selected' : ''">
            {{ membership.name }} {{ membership.amount }}
          </div>
        </div>
        <div class="error-text" v-if="errors.membership_type">
          {{ errors.membership_type[0] }}
        </div>
        <div style="margin-bottom: 35px; margin-top: 35px;">
	  <label class="checkbox-container" v-if="!student">Set my Membership to Auto-renew
	    <input type="checkbox" v-model="auto_renew">
	    <span class="checkmark"></span>
	  </label>
	  <label class="checkbox-container">Join the OWASP Mailing List (See details below)
	    <input type="checkbox" v-model="mailing_list">
	    <span class="checkmark"></span>
	  </label>
        </div>
        <div class="membership-fields">
          <h3>Your Information</h3>
          <div>
            <input type="text" v-model="email" aria-label="Email Address"
            placeholder="Email Address" />
            <div class="error-text" v-if="errors.email">
              {{ errors.email[0] }}
            </div>
          </div>
          <div>
            <input type="text" v-model="email_confirm" aria-label="Confirm Email
            Address" placeholder="Confirm Email Address" />
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
            <input type="text" v-model="name_on_card" aria-label="Name" placeholder="Name" />
            <div class="error-text" v-if="errors.name_on_card">
              {{ errors.name_on_card[0] }}
            </div>
          </div>
        </div>
        <div class="submit-container">
          <button type="submit" class="membership-button" v-bind:disabled="loading">Submit</button>
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
<script src="https://unpkg.com/vue"></script>
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
      mailing_list: false
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
      membershipOptions: function () {
        if (this.student) {
          return [
            { name: 'One Year', amount: '$20', discount: false }
          ];
        }
        if (!this.country || !this.country.hasOwnProperty('discount') ||
        this.country.discount == false) {
          return [
            { name: 'One Year', amount: '$50', discount: false },
            { name: 'Two Year', amount: '$95', discount: false },
            { name: 'Lifetime', amount: '$500', discount: false }
          ];
        } else {
          return [
            { name: 'One Year', amount: '$20', discount: true }
          ]
        }
      }
    },
    watch: {
      country: function (newCountry, oldCountry) {
        if (this.student) {
          return;
        }

        if (newCountry.discount) {
          this.membership_type = 'One Year';
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
        this.loading = true;
        this.validateForm();

        if (Object.keys(this.errors).length > 0) {
          this.loading = false;
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
              vm.$nextTick(function () {
                document.getElementById('error-message').scrollIntoView();
              })
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

        if (!this.membership_type) {
          errors.membership_type = ['Please select a membership type.'];
        }

        if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(this.email)) {
          errors.email = ['Please enter a valid email address'];
        }

        if (this.email_confirm !== this.email) {
          errors.email_confirm = ['Both email addresses must match.'];
        }

        if (!this.name_on_card) {
          errors.name_on_card = ['Please enter your name as it appears on your credit card.'];
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
