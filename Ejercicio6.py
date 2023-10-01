class Cliente:
    def __init__(self, nombre, edad, genero):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero


class Habitacion:
    def __init__(self, numero, tipo, precio):
        self.numero = numero
        self.tipo = tipo
        self.precio = precio


class Hotel:
    def __init__(self):
        self.clientes = []
        self.habitaciones = []
        self.servicios = []

    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)

    def agregar_habitacion(self, habitacion):
        self.habitaciones.append(habitacion)

    def agregar_servicio(self, servicio):
        self.servicios.append(servicio)

    def calcular_monto_total(self):
        monto_reservaciones = sum(h.precio for h in self.habitaciones)
        monto_servicios = sum(s.precio for s in self.servicios)

        return monto_reservaciones + monto_servicios

    def contar_genero(self, genero):
        return sum(1 for cliente in self.clientes if cliente.genero == genero)

    def imprimir_informacion(self):
        print(f"Cantidad de clientes que realizaron reservaciones: {len(self.clientes)}")
        print(f"Monto recaudado por reservaciones y servicios: ${self.calcular_monto_total()}")
        print(f"Cantidad de hombres: {self.contar_genero('Hombre')}")
        print(f"Cantidad de mujeres: {self.contar_genero('Mujer')}")
        print(f"Cantidad de niños: {self.contar_genero('Niño')}")


if __name__ == '__main__':
    cliente1 = Cliente("Pepe", 30, "Hombre")
    cliente2 = Cliente("Fofina", 25, "Mujer")
    cliente3 = Cliente("Juan", 14, "Niño")

    habitacion1 = Habitacion(101, "Doble", 100)
    habitacion2 = Habitacion(102, "Suite", 200)

    servicio1 = Habitacion(101, "Wi-Fi", 10)
    servicio2 = Habitacion(102, "Desayuno", 15)

    hotel = Hotel()
    hotel.agregar_cliente(cliente1)
    hotel.agregar_cliente(cliente2)
    hotel.agregar_cliente(cliente3)
    hotel.agregar_habitacion(habitacion1)
    hotel.agregar_habitacion(habitacion2)
    hotel.agregar_servicio(servicio1)
    hotel.agregar_servicio(servicio2)

    hotel.imprimir_informacion()
