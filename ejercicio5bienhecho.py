import math

class figuras_geometricas:

    def rectangulo(lado, altura):

        return 2 * (lado + altura)

    def triangulo(lado):

        return 3 * lado

    def cirulo(radio):

        return 2 * math.pi * radio

    def regular(lados, cantidad):

        return lados * cantidad


if __name__ == '__main__':
    rectangulo = figuras_geometricas.rectangulo(4, 4)
    triangulo = figuras_geometricas.triangulo(5)
    circulo = figuras_geometricas.cirulo(3)
    regular = figuras_geometricas.regular(5, 4)

    print("Perimetro del rectangulo: ",rectangulo)
    print("Perimetro del triangulo: " ,triangulo)
    print("Perimetro del circulo: " ,circulo)
    print("Perimetro de la figura regular: " ,regular)