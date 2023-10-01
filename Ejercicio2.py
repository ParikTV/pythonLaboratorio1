def verificar_exoneracion(nombre, edad, con_vida, cantidad_propiedades):
    if edad >= 65 and cantidad_propiedades == 1 and con_vida:
        print(nombre, "cumple con la exoneración.")
    else:
        print(nombre, "no cumple con la exoneración.")


Nombre = "Justin Vargas"
Edad = 65
Estado = True
Propiedades = 1

verificar_exoneracion(Nombre, Edad, Estado, Propiedades)
