# Asignatura: Programación Orientada a Objetos
# Flujo principal que instancia y ejecuta los objetos

from mascota import Mascota

def solicitar_datos_mascota(numero):
    """Función auxiliar para registrar los datos por teclado de forma limpia."""
    print(f"\n--- REGISTRO DE LA MASCOTA #{numero} ---")
    nombre = input("Ingrese el nombre: ")
    especie = input("Ingrese la especie (ej. Perro, Gato, Ave): ")
    
    while True:
        try:
            edad = int(input("Ingrese la edad: "))
            if edad >= 0:
                break
            print("La edad no puede ser negativa.")
        except ValueError:
            print("Por favor, ingrese un número entero válido para la edad.")
            
    # Retorna una nueva instancia (objeto) de la clase Mascota
    return Mascota(nombre, especie, edad)


def main():
    print("Bienvenido al Sistema de Gestión de Mascotas (Enfoque POO)")
    print("----------------------------------------------------------")
    
    # El profesor pide crear al menos dos objetos de la clase Mascota
    mascota1 = solicitar_datos_mascota(1)
    mascota2 = solicitar_datos_mascota(2)
    
    # Mostrar la información y ejecutar los métodos de cada objeto
    print("\n--- MOSTRANDO RESULTADOS DE LOS OBJETOS ---")
    
    print("\nDatos de la primera mascota:")
    mascota1.mostrar_informacion()
    mascota1.hacer_sonido()
    
    print("\nDatos de la segunda mascota:")
    mascota2.mostrar_informacion()
    mascota2.hacer_sonido()


if __name__ == "__main__":
    main()