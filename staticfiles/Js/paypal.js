paypal.Buttons({
    style: {
      color: 'blue',
      shape: 'pill',
      label: 'pay'
    },
    
    createOrder: function(data, actions){
      return actions.order.create({
        purchase_units: [{
          amount:{
            value: 495
          }
        }]
      });
    },
    onApprove: function (data, actions){
      actions.order.capture().then(function (detalles){
        window.location.href= "completo.html"
      });
    },
    onCancel: function(data){
      alert("El pago ha sido cancelado")
    }
  }).render('#paypal-button-container');