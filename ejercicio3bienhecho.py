def tragameelo():
    longitud = int(input("Digite la cantidad de empleados "))
    salarios = []

    for i in range(longitud) :
        ingreso = float(input(f"Digite el salario del empleado {i + 1}: "))
        salarios.append(ingreso)

    return salarios, longitud

def promedios(salarios):
    promedio = sum(salarios)

    return promedio


if __name__ == '__main__':
    salarios, longitud = tragameelo()


    promedio = promedios(salarios)

    print("El promedio de",longitud,"es de",promedio)