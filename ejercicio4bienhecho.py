def calcular_promedio(nota1, nota2, nota3):
    promedio = (nota1 + nota2 + nota3) / 3

    return promedio

def sukablad(promedio):
    if promedio >= 70:
        mensaje = "Bimbimbambam"
    elif promedio <= 60:
        mensaje = "Sukablad"
    elif 61 <= promedio <= 69:
        mensaje = "bomboclat"
    else:
        mensaje = "ha ocurrido un error"

    return mensaje


if __name__ == '__main__':
    final = calcular_promedio(60, 21, 80)
    mensaje = sukablad(final)

    print("Su nota es de ", final)
    print(mensaje)