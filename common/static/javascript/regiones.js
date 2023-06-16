function agregarRegionesAlSelect(){
    let jeje = document.getElementById("regiones");
    for (let reg of regiones){
      var opt = document.createElement('option');
      opt.value = reg;
      opt.innerHTML = reg;
      jeje.appendChild(opt);
    }
  }
  const regiones = [
    "Región de Arica y Parinacota",
    "Región de Tarapacá",
    "Región de Antofagasta",
    "Región de Atacama",
    "Región de Coquimbo",
    "Región de Valparaíso",
    "Región del Libertador Gral. Bernardo O’Higgins",
    "Región del Maule",
    "Región de Ñuble",
    "Región del Biobío",
    "Región de la Araucanía",
    "Región de Los Ríos",
    "Región de Los Lagos",
    "Región Aisén del Gral. Carlos Ibáñez del Campo",
    "Región de Magallanes y de la Antártica Chilena",
    "Región Metropolitana de Santiago"
  ]