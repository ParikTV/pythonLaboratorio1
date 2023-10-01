import math


class FigurasGeometricas:

    @staticmethod
    def rectangulo(lado1, lado2):
        return 2 * (lado1 + lado2)

    @staticmethod
    def triangulo_equilatero(lado):
        return 3 * lado

    @staticmethod
    def triangulo_isosceles(lado1, lado2):
        return 2 * lado1 + lado2

    @staticmethod
    def circulo(radio):
        return 2 * math.pi * radio

    @staticmethod
    def poligono_regular(lados, longitud_lado):
        return lados * longitud_lado


if __name__ == '__main__':
    rectangulo = FigurasGeometricas.rectangulo(4, 6)
    triangulo_equilatero = FigurasGeometricas.triangulo_equilatero(5)
    triangulo_isosceles = FigurasGeometricas.triangulo_isosceles(3, 4)
    circulo = FigurasGeometricas.circulo(3)
    poligono_regular = FigurasGeometricas.poligono_regular(5, 4)

    print("Perímetro del rectángulo:", rectangulo)
    print("Perímetro del triángulo equilátero:", triangulo_equilatero)
    print("Perímetro del triángulo isósceles:", triangulo_isosceles)
    print("Perímetro del círculo:", circulo)
    print("Perímetro del polígono regular:", poligono_regular)
