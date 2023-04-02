$(document).ready(function() {
    var traspaso = localStorage.getItem('carrito');
    var carrito = Number(traspaso); 
    $('.cart-counter').text(carrito);
    $('.anadir').click(function() {
      carrito++;
      localStorage.setItem('carrito',carrito); 
    $('.cart-counter').text(carrito);
    });
  });

