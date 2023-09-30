
def cumple_requisitos_exoneracion(nombre, edad, cantidad_propiedades):
    if edad >= 65 and cantidad_propiedades == 1:
        return True
    else:
        return False

nombre_dueño = "Justin"
edad_dueño = 70
cantidad_propiedades = 1

cumple_requisitos = cumple_requisitos_exoneracion(nombre_dueño, edad_dueño, cantidad_propiedades)

if cumple_requisitos:
    print(f"{nombre_dueño} cumple con los requisitos para obtener la exoneración.")
else:
    print(f"{nombre_dueño} no cumple con los requisitos para obtener la exoneración.")
