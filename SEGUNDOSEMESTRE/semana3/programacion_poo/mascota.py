# Asignatura: Programación Orientada a Objetos
# Clase Mascota que representa la abstracción del objeto

class Mascota:
    def __init__(self, nombre, especie, edad):
        """Constructor de la clase: Inicializa los atributos de la mascota."""
        self.nombre = nombre
        self.especie = especie
        self.edad = edad

    def mostrar_informacion(self):
        """Método para mostrar los datos del objeto de forma organizada."""
        print("=================================")
        print(f" Nombre:  {self.nombre}")
        print(f" Especie: {self.especie}")
        print(f" Edad:    {self.edad} años")
        print("=================================")

    def hacer_sonido(self):
        """Método que simula el sonido de la mascota según su especie."""
        # Convertimos a minúsculas para evaluar sin importar cómo lo escriba el usuario
        especie_limpia = self.especie.lower().strip()
        
        if "perro" in especie_limpia:
            print(f"🐾 {self.nombre} dice: ¡Guau! ¡Guau!")
        elif "gato" in especie_limpia:
            print(f"🐾 {self.nombre} dice: ¡Miau! ¡Miau!")
        elif "ave" in especie_limpia or "pajaro" in especie_limpia or "pájaro" in especie_limpia:
            print(f"🐾 {self.nombre} dice: ¡Pío! ¡Pío!")
        else:
            print(f"🐾 {self.nombre} hace un sonido característico de su especie.")