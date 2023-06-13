def agregarMascota(request):
    bandera = False
    if request.method != "POST":
        sexos=Sexo.objects.all();
        context={'sexo':sexos}
        return render(request,'html/agregarMascota.html',context)
    else:
        #Es un POST,por lo tanto se recuperan los datos del formulario
        idMascota=request.POST["idMascota"]
        nombre=request.POST["nombreMascota"]
        fecha_nac=request.POST["fechaNac"]
        raza=request.POST["razaMascota"]
        sexo=request.POST["sexo"]
    
        objSexo=Sexo.objects.get(id_sexo = sexo)
        obj=Mascota(id_mascota=idMascota,
                                   nombre_mascota=nombre,
                                   fecha_nacimiento=fecha_nac,
                                   raza_mascota=raza,
                                   id_sexo=objSexo,
                                   )
        
        mascotas = Mascota.objects.all()
        for m in mascotas:
            if m.id_mascota == obj.id_mascota:
                bandera = True
        if bandera:
            context={'mensaje':'Clave primaria violada'}
            return render(request,'html/agregarMascota.html',context)
        else:
            obj.save()
            context={'mensaje':'OK, datos guardados con éxito'}
            return render(request,'html/agregarMascota.html',context)