---

layout: col-generic
title: Donate
permalink: /donate

---

<!-- Load Stripe.js on your website. -->
<script src="https://js.stripe.com/v3"></script>

<!-- Create a button that your customers click to complete their purchase. Customize the styling to suit your branding. -->
<div class="interactive-wrapper">
    <div class="nav-button">
        <button class="cta-button" id="checkout-button-sku_Fkdcy3MraVedAg" role="link">Donate $25 Now</button>
        <button class="cta-button" id="checkout-button-sku_FkdjHqzhQZCLJk" role="link">Donate $50 Now</button>
    </div>
</div>

<div id="error-message"></div>

<script>
  var stripe = Stripe('pk_test_u4OyMFMbz6tp9sit2bjdHRnT00bac5mrL2');

  var checkoutButton = document.getElementById('checkout-button-sku_Fkdcy3MraVedAg');
  checkoutButton.addEventListener('click', function () {
    // When the customer clicks on the button, redirect
    // them to Checkout.
    stripe.redirectToCheckout({
      items: [{sku: 'sku_Fkdcy3MraVedAg', quantity: 1}],

      // Do not rely on the redirect to the successUrl for fulfilling
      // purchases, customers may not always reach the success_url after
      // a successful payment.
      // Instead use one of the strategies described in
      // https://stripe.com/docs/payments/checkout/fulfillment
      successUrl: 'https://www2.owasp.org/success',
      cancelUrl: 'https://www2.owasp.org/canceled',
      submitType: 'donate',
    })
    .then(function (result) {
      if (result.error) {
        // If `redirectToCheckout` fails due to a browser or network
        // error, display the localized error message to your customer.
        var displayError = document.getElementById('error-message');
        displayError.textContent = result.error.message;
      }
    });
  });

  var checkoutButton = document.getElementById('checkout-button-sku_FkdjHqzhQZCLJk');
  checkoutButton.addEventListener('click', function () {
    // When the customer clicks on the button, redirect
    // them to Checkout.
    stripe.redirectToCheckout({
      items: [{sku: 'sku_FkdjHqzhQZCLJk', quantity: 1}],

      // Do not rely on the redirect to the successUrl for fulfilling
      // purchases, customers may not always reach the success_url after
      // a successful payment.
      // Instead use one of the strategies described in
      // https://stripe.com/docs/payments/checkout/fulfillment
      successUrl: 'https://www2.owasp.org/success',
      cancelUrl: 'https://www2.owasp.org/canceled',
      submitType: 'donate',
    })
    .then(function (result) {
      if (result.error) {
        // If `redirectToCheckout` fails due to a browser or network
        // error, display the localized error message to your customer.
        var displayError = document.getElementById('error-message');
        displayError.textContent = result.error.message;
      }
    });
  });
</script>