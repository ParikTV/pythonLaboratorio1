
def calcular_promedio_salarios(empleados):
    if not empleados:
        return 0

    total_salarios = sum(empleados)
    promedio = total_salarios / len(empleados)
    return promedio



salarios_empleados = [30000, 35000, 40000]

promedio_general = calcular_promedio_salarios(salarios_empleados)
print(f"El promedio general de salarios de los empleados es: {promedio_general}")
