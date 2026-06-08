# Definición de la clase PanelAlarma
class PanelAlarma:
    def __init__(self, modelo, zonas_activas):
        self.modelo = modelo
        self.zonas_activas = zonas_activas
        self.estado = "Desactivado"

    def activar(self):
        self.estado = "Activado"
        print("El panel de alarma ha sido activado.")

    def desactivar(self):
        self.estado = "Desactivado"
        print("El panel de alarma ha sido desactivado.")

    def mostrar_estado(self):
        print("Información del panel de alarma:")
        print(f"Modelo: {self.modelo}")
        print(f"Zonas activas: {self.zonas_activas}")
        print(f"Estado actual: {self.estado}")


# Creación de objetos
panel1 = PanelAlarma("DSC PowerSeries", 8)
panel2 = PanelAlarma("Paradox EVO", 16)

# Uso de métodos
panel1.mostrar_estado()
panel1.activar()

print()  # Separador visual

panel2.mostrar_estado()
panel2.desactivar()