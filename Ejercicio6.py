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

class ServicioAdicional:
    def __init__(self, nombre, costo):
        self.nombre = nombre
        self.costo = costo

class Reservacion:
    def __init__(self, cliente, habitacion, servicios_adicionales=[]):
        self.cliente = cliente
        self.habitacion = habitacion
        self.servicios_adicionales = servicios_adicionales

    def calcular_costo_total(self):
        costo_habitacion = self.habitacion.precio
        costo_servicios = sum(servicio.costo for servicio in self.servicios_adicionales)
        return costo_habitacion + costo_servicios

# Ejemplo de uso
# Crear clientes
cliente1 = Cliente("Cristiano Ronaldo", 35, "Hombre")
cliente2 = Cliente("Alexa Rodriguez", 28, "Mujer")
cliente3 = Cliente("Neymar Junior", 10, "Niño")

# Crear habitaciones
habitacion1 = Habitacion(101, "Doble", 100)
habitacion2 = Habitacion(201, "Suite", 200)
habitacion3 = Habitacion(301, "Individual", 80)

# Crear servicios adicionales
servicio1 = ServicioAdicional("Desayuno", 10)
servicio2 = ServicioAdicional("Wi-Fi", 5)
servicio3 = ServicioAdicional("Estacionamiento", 15)

# Crear reservaciones
reservacion1 = Reservacion(cliente1, habitacion1, [servicio1, servicio2])
reservacion2 = Reservacion(cliente2, habitacion2, [servicio3])
reservacion3 = Reservacion(cliente3, habitacion3, [servicio1])

# Calcular la cantidad de clientes que realizaron reservaciones
cantidad_clientes = len([reservacion1, reservacion2, reservacion3])

# Calcular el monto recaudado por concepto de reservaciones y servicios brindados
monto_total = sum(reservacion.calcular_costo_total() for reservacion in [reservacion1, reservacion2, reservacion3])

# Calcular la cantidad de hombres, mujeres y niños que se hospedaron en el hotel
cantidad_hombres = sum(1 for cliente in [cliente1] if cliente.genero == "Hombre")
cantidad_mujeres = sum(1 for cliente in [cliente2] if cliente.genero == "Mujer")
cantidad_ninos = sum(1 for cliente in [cliente3] if cliente.edad < 18)

# Imprimir resultados
print(f"Cantidad de clientes que realizaron reservaciones: {cantidad_clientes}")
print(f"Monto recaudado por concepto de reservaciones y servicios: ${monto_total}")
print(f"Cantidad de hombres: {cantidad_hombres}")
print(f"Cantidad de mujeres: {cantidad_mujeres}")
print(f"Cantidad de niños: {cantidad_ninos}")
