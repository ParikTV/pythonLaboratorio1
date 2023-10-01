def calcular_promedio(nota1, nota2, nota3):
    promedio = (nota1 + nota2 + nota3) / 3

    return promedio


def promedios(promedio):
    if promedio >= 70:
        mensajes = "Aprobado"
    elif promedio <= 60:
        mensajes = "Reprobado"
    elif 61 <= promedio <= 69:
        mensajes = "Sustitucion pa"
    else:
        mensajes = "ha ocurrido un error"

    return mensajes


if __name__ == '__main__':
    final = calcular_promedio(60, 50, 80)
    mensaje = promedios(final)

    print("Su nota es de ", final)
    print(mensaje)
