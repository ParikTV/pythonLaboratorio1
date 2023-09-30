import math
class CalculadoraPerimetros:
    def calcular_perimetro(self, forma, *args):
        if forma == "rectangulo":
            if len(args) == 2:
                a, b = args
                return 2 * (a + b)
            else:
                raise ValueError("Se requieren dos lados para calcular el perímetro de un rectángulo.")
        elif forma == "triangulo":
            if len(args) == 1:
                lado = args[0]
                return 3 * lado
            elif len(args) == 2:
                lado1, lado2 = args
                return 2 * lado1 + lado2
            else:
                raise ValueError("Se requieren uno o dos lados para calcular el perímetro de un triángulo.")
        elif forma == "circulo":
            if len(args) == 1:
                radio = args[0]
                return 2 * math.pi * radio
            else:
                raise ValueError("Se requiere el radio para calcular el perímetro de un círculo.")
        elif forma == "poligono_regular":
            if len(args) == 2:
                numero_lados, longitud_lado = args
                return numero_lados * longitud_lado
            else:
                raise ValueError("Se requieren el número de lados y la longitud del lado para calcular el perímetro de un polígono regular.")
        else:
            raise ValueError("Forma geométrica no reconocida.")

# Ejemplo de uso
calculadora = CalculadoraPerimetros()
perimetro_rectangulo = calculadora.calcular_perimetro("rectangulo", 4, 6)
perimetro_triangulo = calculadora.calcular_perimetro("triangulo", 5)
perimetro_circulo = calculadora.calcular_perimetro("circulo", 3)
perimetro_poligono = calculadora.calcular_perimetro("poligono_regular", 5, 4)

print(f"Perímetro del rectángulo: {perimetro_rectangulo}")
print(f"Perímetro del triángulo: {perimetro_triangulo}")
print(f"Perímetro del círculo: {perimetro_circulo}")
print(f"Perímetro del polígono regular: {perimetro_poligono}")
