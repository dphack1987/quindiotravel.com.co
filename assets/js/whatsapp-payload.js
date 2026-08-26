(function () {
  if (document.querySelector('script[data-whatsapp-payload-builder]')) return;

  var script = document.createElement('script');
  script.src = '/assets/js/whatsapp-payload-builder.js';
  script.defer = true;
  script.dataset.whatsappPayloadBuilder = 'true';
  document.head.appendChild(script);
})();
