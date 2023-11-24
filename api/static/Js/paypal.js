paypal.Buttons({
    style: {
      color: '',
      shape: '',
      label: ''
    },
    
    createOrder: function(data, actions){
      return actions.order.create({
        purchase_units: [{
          amount:{
            value: 350
          }
        }]
      });
    },
    onApprove: function (data, actions){
      actions.order.capture().then(function (detalles){
        window.location.href=""
      });
    },
    onCancel: function(data){
      alert("El pago ha sido cancelado")
    }
  }).render('#paypal-button-container');