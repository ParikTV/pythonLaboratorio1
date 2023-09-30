
def estado_alumno(promedio):
    if promedio >= 70:
        return "Aprobado"
    elif promedio < 60:
        return "Reprobado"
    else:
        return "Sustitución"

def sacar_promedio(nota 1, nota2, nota3):
    promedio = (nota1 + nota2 + nota3) / 3

resultado = estado_alumno(promedio_alumno)
print(f"El estado del alumno es: {resultado}")
