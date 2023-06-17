function agregarRegionesAElElemento(){
  console.log("hola")
  /*let jeje = document.getElementById("regiones");
  for (let reg of regiones){
    console.log(reg)
    var opt = document.createElement('option');
    opt.value = reg;
    opt.innerHTML = reg;
    jeje.appendChild(opt);
  }*/
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

function verificarRegionyComuna() {
  const reggion = document.getElementById('regiones').value;
  const communa = document.getElementById('comuna').value;
  if (reggion == "seleccion" || communa == "comuna") {
    return false;
  }
  else {
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

function verificarRutdelCliente(){
  var run=document.getElementById('rut').value;
  if (parseInt(run)<2000000 || parseInt(run)>40000000){
    document.getElementById('invalid-run').textContent = "El rut ingresado no corresponde.";
    return false;
  }else {
    document.getElementById('invalid-run').textContent = "";
    return true;
  }
}

function verificarTelefonodelCliente(){
  var numero=document.getElementById('telefono').value;
    
  if (parseInt(numero)<11111111 || parseInt(numero)>99999999){
    document.getElementById('invalid-fono').textContent = "El número de teléfono ingresado no corresponde.";
    return false;
  }else {
    document.getElementById('invalid-fono').textContent = "";
    return true;
  }
}

function verificarDirecciondelCliente(){
  var direccion=document.getElementById('direccion').value; 
  if (direccion.length<10){
    document.getElementById('invalid-direccion').textContent = "La dirección ingresada es muy corta. Intenta nuevamente.";
    return false;
  }else {
    document.getElementById('invalid-direccion').textContent = "";
    return true;
  }
}

let formulario = document.getElementById('crearUsuario');

formulario.addEventListener("submit", (e) => {
  if (!verificarEmailUser() || !verificarLargoNombre() || !verificarApellidoCliente() || !verificarRegionyComuna() || !verificarRutdelCliente() ||!verificarTelefonodelCliente()) {
    verificarApellidoCliente();
    verificarRegionyComuna();
    verificarEmailUser();
    verificarLargoNombre();
    verificarRutdelCliente();
    verificarTelefonodelCliente()
    e.preventDefault();
  }
}
);


