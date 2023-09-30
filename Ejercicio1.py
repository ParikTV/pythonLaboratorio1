from datetime import datetime


class Breteador:
    def __init__(self, nombre, fecha_ingreso):
        self.nombre = nombre
        self.fecha_ingreso = fecha_ingreso

    def calcular_ayo_servicio(self):
        fecha_actual = datetime.now()
        ayo_actual = fecha_actual.year
        ayo_ingreso = self.fecha_ingreso.year

        ayo_servicio = ayo_actual - ayo_ingreso

        return ayo_servicio

    def aplicar_bonificacion(self):
        ayo_servicio = self.calcular_ayo_servicio()
        bonificacion = 0

        if ayo_servicio >= 5 and ayo_servicio < 10:
            bonificacion = 1000
        elif ayo_servicio >= 10 and ayo_servicio < 15:
            bonificacion = 2000
        elif ayo_servicio >= 15:
            bonificacion = 3000

        return bonificacion


fecha_ingreso_empleado = datetime(2003, 7, 18)
empleado = Breteador("Justin", fecha_ingreso_empleado)
anios_servicio = empleado.calcular_ayo_servicio()
bonificacion = empleado.aplicar_bonificacion()

print(f"{empleado.nombre} ha trabajo {anios_servicio} años.")
print(f"Bonificacion por años de servicio: {bonificacion}")
