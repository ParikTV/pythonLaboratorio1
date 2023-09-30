def verificar_exoneracion(nombre, edad, con_vida, cantidad_propiedades):
    if edad >= 65 and cantidad_propiedades == 1 and con_vida:
        print(f"{nombre} cumple con la exoneración.")
    else:
        print(f"{nombre} no cumple con la exoneración.")

nombre_dueño = "Justin Vargas"
edad_dueño = 70
con_vida = True
cantidad_propiedades = 1

verificar_exoneracion(nombre_dueño, edad_dueño, con_vida, cantidad_propiedades)
