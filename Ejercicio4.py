
def estado_alumno(promedio):
    if promedio >= 70:
        return "Aprobado"
    elif promedio < 60:
        return "Reprobado"
    else:
        return "Sustitución"


promedio_alumno = 75

resultado = estado_alumno(promedio_alumno)
print(f"El estado del alumno es: {resultado}")
