$(document).ready(function () {
    'use strict'
    const forms = document.querySelectorAll('.needs-validation')
    Array.from(forms)
    .forEach(function (form) {
        form.addEventListener('submit', function (event) {
        
        if (!form.checkValidity()) {
            event.preventDefault()
            event.stopPropagation()
        }else{
          var usuario = document.getElementById('usuario').value;
          var contrasenia = document.getElementById('contrasenia').value;
          alert("Cliente agregado exitosamente\nUsuario: "+usuario+"\nContraseña: "+contrasenia);
          localStorage.setItem('user',usuario);
          localStorage.setItem('pass',contrasenia);
        }
  
        form.classList.add('was-validated')
        }, false)
    })
  });