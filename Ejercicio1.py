import datetime


class Breteador:
    def __init__(self, nombre, fecha_ingreso):
        self.nombre = nombre
        self.fecha_ingreso = fecha_ingreso

    def calcular_ayo_servicio(self):
        fecha_actual = datetime.datetime.now()
        ayo_actual = fecha_actual.year
        ayo_ingreso = self.fecha_ingreso.year

        ayo_servicio = ayo_actual - ayo_ingreso

        return ayo_servicio

    def calcular_bonificacion(self):
        ayo_servicio = self.calcular_ayo_servicio()

        if ayo_servicio <= 5:
            bonificaciones = 0.02
        elif 6 <= ayo_servicio <= 10:
            bonificaciones = 0.05
        elif 11 <= ayo_servicio <= 25:
            bonificaciones = 0.10
        else:
            bonificaciones = 0

        salario = 100
        bonificacion_total = salario * bonificaciones

        return bonificacion_total


fecha_ingreso_empleado = datetime.datetime(2003, 7, 12)
empleado = Breteador("Justin", fecha_ingreso_empleado)
anios_servicio = empleado.calcular_ayo_servicio()
bonificacion = empleado.calcular_bonificacion()

print(empleado.nombre, " ha trabajado ", anios_servicio, "años.")
print(f"Bonificación por años de servicio: {bonificacion:.2f}")
