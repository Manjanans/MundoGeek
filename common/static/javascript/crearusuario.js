const region = ["Región de Arica y Parinacota",];

$(document).ready(function () {
  $.get("../javascript/comunas.json",
    function (data) {
      $.each(data.regiones, function (i, item) {
        $("#regiones").append("<option value='" + item.region + "'>" + item.region + "</option>");
      });
    });
});

function cambioDeComunaXRegion() {
  var comuna;
  document.getElementById("comuna").innerHTML = "<option value='selec'>Seleccione la comuna</option>";
  $(document).ready(function () {
    $.get("../javascript/comunas.json",
      function (data) {
        $.each(data.regiones, function (i, item) {
          if (document.getElementById('regiones').value == item.region) {
            comuna = item.comunas;
            for (var i = 0; i < comuna.length; i++) {
              $("#comuna").append("<option value='" + comuna[i] + "'>" + comuna[i] + "</option>");
            }
          }
        });
      });
  });
}

function verificarEmailUser() {
  const email = document.getElementById('email').value;
  if (email.length < 6 || email.length > 30) {
    document.getElementById('invalid-email').textContent = "El usuario de email debe tener entre 6 y 30 caracteres. Intenta nuevamente.";
    return false;
  }
  else {
    document.getElementById('invalid-email').textContent = "";
    return true;
  }
}

function verificarLargoNombre() {
  const nombre = document.getElementById('nombre').value;
  if (nombre.length < 3) {
    document.getElementById('invalid-name').textContent = "Nombre ingresado es muy corto. Debe ser de al menos 3 caracteres de largo.";
    return false;
  }
  else {
    document.getElementById('invalid-name').textContent = "";
    return true;
  }
}

function verificarApellidoCliente() {
  const apellido = document.getElementById('apellido').value;
  if (apellido.length < 3) {
    document.getElementById('invalid-lastname').textContent = "Apellido ingresado es muy corto. Debe ser de al menos 3 caracteres de largo.";
    return false;
  }
  else {
    document.getElementById('invalid-lastname').textContent = "";
    return true;
  }
}

function verificarLargoUsuario() {
  const user = document.getElementById('usuario').value;
  if (user.length < 6) {
    document.getElementById('invalid-user').textContent = "Usuario ingresado es muy corto. Debe ser de al menos 6 caracteres de largo.";
    return false;
  }
  else {
    document.getElementById('invalid-user').textContent = "";
    return true;
  }
}

function largoContrasenia(largo) {
  if (largo < 8) {
    document.getElementById('pass-largo').textContent = "La contraseña debe tener al menos 8 caracteres."
    document.getElementById('pass-largo').style.color = "red";
    return false;
  } else {
    document.getElementById('pass-largo').style.color = "green";
    return true;
  }
}

function contieneMayuscula(pass) {
  return /[A-Z]/.test(pass);
}

function contieneCaracterEspecial(pass) {
  return /[@_*(),%]/.test(pass);
}

function contieneNumeroStr(pass) {
  return /[0-9]/.test(pass);
}

function mayusEnContrasenia(pass) {
  if (!contieneMayuscula(pass)) {
    document.getElementById('pass-mayus').textContent = "La contraseña debe tener al menos 1 caracter en mayúsculas."
    document.getElementById('pass-mayus').style.color = "red";
    return false;
  }
  else {
    document.getElementById('pass-mayus').style.color = "green";
    return true;
  }
}

function especialEnContrasenia(pass) {
  if (!contieneCaracterEspecial(pass)) {
    document.getElementById('pass-especial').textContent = "La contraseña debe tener al menos un caracter especial ej: (@,_,*,(,),%)."
    document.getElementById('pass-especial').style.color = "red";
    return false;
  }
  else {
    document.getElementById('pass-especial').style.color = "green";
    return true;
  }
}

function contraseniaTieneNum(pass) {
  if (!contieneNumeroStr(pass)) {
    document.getElementById('pass-num').textContent = "La contraseña debe contener al menos un número."
    document.getElementById('pass-num').style.color = "red";
    return false;
  } else {
    document.getElementById('pass-num').style.color = 'green';
    return true;
  }
}

function verificarContraseniaUsuario() {
  var pass = document.getElementById('contrasenia').value;
  var largo = pass.length;
  if (!largoContrasenia(largo) || !mayusEnContrasenia(pass) || !especialEnContrasenia(pass) || !contraseniaTieneNum(pass)) {
    largoContrasenia(largo);
    mayusEnContrasenia(pass);
    especialEnContrasenia(pass);
    contraseniaTieneNum(pass);
    return false;
  } else {
    return true;
  }
}

let formulario = document.getElementById('crearUsuario');

formulario.addEventListener("submit", (e) => {
  if (!verificarEmailUser() || !verificarLargoNombre() || !verificarApellidoCliente() || !verificarLargoUsuario() || !verificarContraseniaUsuario()) {
    alert("Le faltan ingresar datos.\nRellene el formulario correctamente.");
    verificarApellidoCliente();
    verificarContraseniaUsuario();
    verificarEmailUser();
    verificarLargoNombre();
    verificarLargoUsuario();
    e.preventDefault();
  } else {
    const nombre = document.getElementById('nombre').value;
    const apellido = document.getElementById('apellido').value;
    const mail = document.getElementById('email').value + '@' + document.getElementById('server').value;
    const user = document.getElementById('usuario').value;
    const pass = document.getElementById('contrasenia').value;
    const region = document.getElementById('regiones').value;
    const comuna = document.getElementById('comuna').value;
    const nuevo = new cliente(nombre, apellido, mail, user, pass, region, comuna);
    alert("Usuario creado exitosamente.\nUsuario: " + nuevo.user + "\nContraseña: " + nuevo.pass);
    localStorage.setItem("cliente", JSON.stringify(nuevo));
  }
}
);      