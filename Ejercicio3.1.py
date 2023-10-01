def verificar_exoneracion(edad, propiedades):
    return edad >= 65 and propiedades == 1


Nombre = "Justin Vargas"
Edad = 65
Propiedades = 1

cumple_exoneracion = verificar_exoneracion(Edad, Propiedades)

if cumple_exoneracion:
    print(Nombre, "Cumple con la exoneración.")
else:
    print(Nombre, "No cumple con la exoneración.")
