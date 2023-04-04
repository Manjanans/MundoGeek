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
            const us = localStorage.getItem('user');
            const pw = localStorage.getItem('pass');

            var user = document.getElementById('usuario').value;
            var pass = document.getElementById('contrasenia').value;

            if(us == user && pw==pass){
                alert("Ingreso exitoso\nUsuario: "+user+"\nContraseña: "+pass);
            }else{
                alert("Los datos no coinciden.\nIntente nuevamente.");
            }
            
        }
  
        form.classList.add('was-validated')
        }, false)
    })
  });