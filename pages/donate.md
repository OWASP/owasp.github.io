---

layout: full-width
title: Donate to Open Source Security Projects
permalink: /donate/

---

<style>
[v-cloak] {display: none}

.legal-text {
  font-size: 75%;
  color: #808080;
}

.form-container {
  margin: 40px 0px;
  max-width: 100%;
}

.amount-title {
  align-self: center;
}

.gift-amount-header {
  display: flex;
  justify-content: space-between;
  flex-direction: row;
  font-size: 80%;
  margin-bottom: 8px;
}

.gift-currency {
  display: flex;
}

.gift-currency div {
  background-color: #D3D3D3;
  padding: 6px;
  margin: 0px 2px;
  cursor: pointer;
}

.gift-currency div.selected {
  background-color: #233e81;
  color: #ffffff;
  font-weight: bold;
}

.gift-currency div:last-child {
  margin-right: 0px;
}

.donation-options {
  margin: 20px 0px 40px 0px;
}

.donor-fields {
  margin-bottom: 40px;
}

.donor-fields div {
  margin: 14px 0px;
}

.donor-fields input {
  width: 100%;
  border: 1px solid #000000;
  padding: 8px;
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

.donate-button {
  border: 0;
  padding: 16px;
  font-weight: bold;
  color: #ffffff;
  background-color: #233e81;
  text-transform: uppercase;
  font-size: 110%;
}


.donation-amount-row div {
  text-align: center;
  background-color: #D3D3D3;
  color: #000000;
  padding: 20px;
  margin: 8px 0px;
  font-weight: bold;
  cursor: pointer;
}

.donation-amount-row div.selected {
  color: #ffffff;
  background-color: #233e81;
}

.currencyinput {
  background-color: #ffffff;
  color: #000000;
  border: 1px solid #ffffff;
}

.currencyinput input {
  font-size: 18px;
  border: 0;
  max-width: 100px;
  padding-left: 12px;
}

.error-text {
  color: #ff0000;
  font-size: 75%;
  margin-top: 4px !important;
}

.form-container input:focus {
  outline: none;
}

@media (min-width: 768px) {
  .form-container {
    max-width: 70%;
  }

  .donation-amount-row {
    display: flex;
    flex-direction: row;
  }

  .donation-amount-row div {
    flex: 1;
    flex-basis: 0;
    margin: 8px;
  }

  .donation-amount-row div:first-child {
    margin-left: 0;
  }

  .donation-amount-row div:last-child {
    margin-right: 0;
  }
}
</style>

{% raw %}
<div id="donate-app" style="margin: 0px;" v-cloak>

  <div class="col-sidebar">
    <div class="main-wrapper" style="padding: 0px;">
      <div>

      <!-- main donation form -->

      <h1>Donate to the OWASP Foundation</h1>

      <p>The Open Web Application Security Project (OWASP) is a nonprofit
      foundation that works to improve the security of software. Through community-led open
      source software projects and hundreds of local chapters worldwide, your gift* will support the Foundation and its many activities
      around the world to secure the web. Existing donors can <a href="/manage-membership">Modify Recurring Gifts</a>.</p>


      <form class="form-container" v-on:submit.prevent="handleSubmit">
        <vue-recaptcha sitekey="6LfsuK4ZAAAAAOEQWvk5zkD9K00uURbviflRH_8M" v-on:verify="onVerifyCaptcha" ref="invisibleRecaptcha" size="invisible" v-on:expired="onExpiredCaptcha" v-on:error="onCaptchaError"></vue-recaptcha>
        <div class="error-text" style="font-size: 90%; margin-bottom: 16px" id="error-message" v-if="Object.keys(errors).length">
          Please correct the errors below before proceeding.
        </div>
        <div class="gift-amount">
          <div class="gift-amount-header">
            <div class="amount-title">Amount of your Gift</div>
            <div class="gift-currency">
              <div v-bind:class="currency === 'usd' ? 'selected' : ''" v-on:click="changeCurrency('usd')">USD &#36;</div>
              <div v-bind:class="currency === 'eur' ? 'selected' : ''" v-on:click="changeCurrency('eur')">EUR &#8364;</div>
              <div v-bind:class="currency === 'gbp' ? 'selected' : ''" v-on:click="changeCurrency('gbp')">GBP &#163;</div>
            </div>
          </div>
          <div class="donation-amounts">
            <div class="donation-amount-row">
              <div v-on:click="setAmount(10)" v-bind:class="amount === 10 &&
              !isCustomAmount ? 'selected' : ''">
                <span v-html="currencySymbol"></span>10
              </div>
              <div v-on:click="setAmount(25)" v-bind:class="amount === 25 &&
              !isCustomAmount ? 'selected' : ''">
                <span v-html="currencySymbol"></span>25
              </div>
              <div v-on:click="setAmount(50)" v-bind:class="amount === 50 &&
              !isCustomAmount ? 'selected' : ''">
                <span v-html="currencySymbol"></span>50
              </div>
            </div>
            <div class="donation-amount-row">
              <div v-on:click="setAmount(100)" v-bind:class="amount === 100 &&
              !isCustomAmount ? 'selected' : ''">
                <span v-html="currencySymbol"></span>100
              </div>
              <div v-on:click="setAmount(500)" v-bind:class="amount === 500 &&
              !isCustomAmount ? 'selected' : ''">
                <span v-html="currencySymbol"></span>500
              </div>
              <div v-on:click="setCustomAmount" v-bind:class="isCustomAmount ? 'selected' : ''">
                <span v-if="!isCustomAmount">Other</span>
                <span class="currencyinput" v-else><span
                v-html="currencySymbol"></span><input type="text"
                v-model="amount" placeholder="Amount" id="custom-amount-field"></span>
              </div>
            </div>
          </div>
          <div class="error-text" v-if="errors.amount">
            {{ errors.amount[0] }}
          </div>
        </div>
        <div class="donation-options">
	  <label class="checkbox-container">Make this a monthly recurring gift
	    <input type="checkbox" v-model="recurring">
	    <span class="checkmark"></span>
	  </label>
	  <label class="checkbox-container">Join the OWASP Mailing List
	    <input type="checkbox" v-model="mailing_list">
	    <span class="checkmark"></span>
	  </label>
          <label class="checkbox-container" v-if="projectName">Publicly list me as a supporter of <span style="font-weight: 900; color: #233e81">{{ projectName }}</span>
	    <input type="checkbox" v-model="attribution">
	    <span class="checkmark"></span>
	  </label>
        </div>
        <div class="donor-fields">
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
          <div>
            <input type="text" v-model="name" aria-label="Name" placeholder="Name" />
            <div class="error-text" v-if="errors.name">
              {{ errors.name[0] }}
            </div>
          </div>
        </div>
        <div class="donation-options" v-if="showRestrictedOption">
          <label class="checkbox-container">Please restrict this gift<span v-if="projectName"> for <span style="font-weight: 900; color: #233e81">{{ projectName }}</span></span>. In doing so, I understand this gift amount is net 15% administration costs and unspent restricted gift balances become unrestricted at the end of each calendar year.
	    <input type="checkbox" v-model="restricted">
	    <span class="checkmark"></span>
	  </label>
        </div>
        <div class="submit-container">
          <button type="submit" class="donate-button" v-bind:disabled="loading">Donate</button>
        </div>
      </form>

      <p class="legal-text">* Unless otherwise noted your gift to the OWASP Foundation, net credit card processing fees,
      is unrestricted and will be used at the sole discretion of the
      organization to fulfill its mission and objectives. Read more about our <a href="/www-policy/operational/donations" target="_blank" rel="noopener">Donation Policy</a>. You do have the option
      to be listed as a Supporter of a Project or Chapter; however, this option
      does not restrict your gift in anyway whatsoever. The OWASP Foundation is
      a 501(c)3 therefore in some cases your gift may be tax-deductible and you
      should consult with a tax professional for more details. Additionally you can elect to receive marketing mails from us by  selecting "Join the OWASP Marketing Mail List." Marketing mails include information and special offers for upcoming conferences, meetings, and other opportunities offered to you. You can revoke your consent to receive Marketing Mail List emails at any time by using the Unsubscribe link found at the bottom of these emails.</p>

      <!-- end donation form -->

      </div>
      <aside class="sidebar" role="complementary">
        <!-- reserved for future use -->
      </aside>
    </div>
  </div>

</div>


{% endraw %}

<script src="https://www.google.com/recaptcha/api.js?onload=vueRecaptchaApiLoaded&render=explicit"></script>
<script src="https://js.stripe.com/v3"></script>
<script src="https://unpkg.com/vue"></script>
<script src="https://unpkg.com/axios/dist/axios.min.js"></script>
<script src="https://unpkg.com/vue-recaptcha@latest/dist/vue-recaptcha.min.js"></script>

<script>
var stripe = Stripe('pk_live_mw0B2kiXQTFkD44liAEI03oT00S5AGfSV3');
window.addEventListener('load', function () {
  new Vue({
    el: '#donate-app',
    components: {
      VueRecaptcha: window.VueRecaptcha
    },
    data: {
      amount: 50,
      isCustomAmount: false,
      currency: 'usd',
      recurring: false,
      mailing_list: false,
      attribution: false,
      restricted: false,
      projectName: null,
      repoName: null,
      email: null,
      email_confirm: null,
      name: null,
      source: null,
      loading: false,
      errors: {}
    },
    computed: {
      currencySymbol: function () {
        if (this.currency === 'usd') {
          return '&#x24;';
        }
        if (this.currency === 'eur') {
          return '&#8364;';
        }

        return '&#163;';
      },
      showRestrictedOption: function () {
        if (this.amount >= 1000) {
          return true;
        }
        return false;
      }
    },
    watch: {
      amount: function (newAmount) {
        if (newAmount < 1000) {
          this.restricted = false;
        }
      }
    },
    created: function () {
      const queryParams = new URLSearchParams(window.location.search);
      if (queryParams.has('title')) {
        this.projectName = queryParams.get('title');
      }
      if (queryParams.has('reponame')) {
        this.repoName = queryParams.get('reponame');
      }
      if (queryParams.has('currency') && ['usd', 'eur', 'gbp'].includes(queryParams.get('currency'))) {
        this.currency = queryParams.get('currency');
      }
      if (queryParams.has('restricted') && queryParams.get('restricted') ==
      'yes') {
        this.setCustomAmount();
        this.amount = 1001;
        this.restricted = true;
      }
    },
    methods: {
      handleSubmit: function () {
        let vm = this;
        vm.loading = true;
        this.validateForm();

        if (Object.keys(vm.errors).length > 0) {
          vm.loading = false;
          vm.$nextTick(function () {
            document.getElementById('error-message').scrollIntoView();
          })
        } else {
          this.$refs.invisibleRecaptcha.execute()
        }
      },
      changeCurrency: function (currency) {
        this.currency = currency;
      },
      setAmount: function (amount) {
        this.amount = amount;
        this.isCustomAmount = false;
      },
      setCustomAmount: function () {
        if (!this.isCustomAmount) {
          this.amount = null;
          this.isCustomAmount = true;
          this.$nextTick(function () {
            document.getElementById('custom-amount-field').focus()
          })
        }
      },
      validateForm: function () {
        let errors = {};

        if (!this.amount) {
          errors.amount = ['Please select a donation amount.'];
        } else {
          if ((typeof this.amount === 'string' || this.amount instanceof String) && !this.amount.match(/^-{0,1}\d+$/)) {
            errors.amount = ['Donation amounts must be whole numbers between 10 and 5000 with no commas or decimals.'];
          } else {
            let intAmount = parseInt(this.amount)
            if (intAmount < 10 || intAmount > 5000) {
              errors.amount = ['Donation amounts must be whole numbers between 10 and 5000 with no commas or decimals.'];
            }
          }
        }

        if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(this.email)) {
          errors.email = ['Please enter a valid email address'];
        }

        if (this.email_confirm !== this.email) {
          errors.email_confirm = ['Both email addresses must match.'];
        }

        if (!this.name) {
          errors.name = ['Please enter your name as it appears on your credit card.'];
        }

        this.errors = errors;
      },
      onVerifyCaptcha: function () {
        let vm = this;
        const postData = {
          checkout_type: 'donation',
          amount: vm.amount,
          currency: vm.currency,
          recurring: vm.recurring,
          attribution: vm.attribution,
          project_title: vm.projectName,
          repo_name: vm.repoName,
          mailing_list: vm.mailing_list,
          restricted: vm.restricted,
          email: vm.email,
          name: vm.name,
          source: vm.source
        };

        axios.post('https://owaspadmin.azurewebsites.net/api/CreateCheckoutSession?code=ulMNYVfgzBytI1adat1lS6MQ3NabtwKE4IgCJ8yKuhvbFoQh6nOYaw==', postData).then(function (response) {
          stripe.redirectToCheckout({
            sessionId: response.data.data.session_id
          }).then(function (result) {
            console.log(result.error.message)
          }); 
        }).catch(function (error) {
          vm.errors = error.response.data.errors
          vm.loading = false
          vm.$nextTick(function () {
            document.getElementById('error-message').scrollIntoView();
          })
        });
      },
      onExpiredCaptcha: function () {
        this.loading = false
      },
      onCaptchaError: function () {
        this.loading = false
      }
    }
  })
}, false)
</script>

