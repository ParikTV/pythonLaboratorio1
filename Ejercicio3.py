def calcular_promedio_general():
    cantidad_empleados = int(input("Digite la cantidad de empleados: "))
    salarios = []

    for i in range(cantidad_empleados):
        salario = float(input(f"Digite el salario del empleado {i + 1}: "))
        salarios.append(salario)

    promedios_general = sum(salarios) / cantidad_empleados
    return promedios_general


if __name__ == '__main__':
    promedio_general = calcular_promedio_general()
    print("El promedio general de los empleados es:", promedio_general)
