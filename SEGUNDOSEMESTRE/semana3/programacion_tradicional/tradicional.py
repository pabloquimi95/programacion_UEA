# Asignatura: Programación Orientada a Objetos
# Tarea Semana 3 - Programa 1: Programación Tradicional

def registrar_mascota():
    """Función para solicitar los datos de la mascota por teclado."""
    print("--- REGISTRO DE LA MASCOTA ---")
    nombre = input("Ingrese el nombre de la mascota: ")
    especie = input("Ingrese la especie (ej. Perro, Gato, Ave): ")
    
    # Validamos que la edad sea un número entero válido
    while True:
        try:
            edad = int(input("Ingrese la edad de la mascota (en años): "))
            if edad >= 0:
                break
            else:
                print("Por favor, ingrese una edad válida (mayor o igual a 0).")
        except ValueError:
            print("Entrada inválida. Debe ingresar un número entero para la edad.")
            
    # Retornamos los datos en una tupla
    return nombre, especie, edad


def mostrar_mascota(nombre, especie, edad):
    """Función para mostrar la información registrada de forma organizada."""
    print("\n=================================")
    print("      INFORMACIÓN DE LA MASCOTA    ")
    print("=================================")
    print(f" Nombre:  {nombre}")
    print(f" Especie: {especie}")
    print(f" Edad:    {edad} años")
    print("=================================\n")


def main():
    """Función principal que controla el flujo del programa."""
    print("Bienvenido al Sistema de Gestión de Mascotas (Enfoque Tradicional)")
    print("-----------------------------------------------------------------")
    
    # Llamamos a la función para registrar y guardamos los datos en variables
    nombre_m, especie_m, edad_m = registrar_mascota()
    
    # Llamamos a la función para mostrar los resultados
    mostrar_mascota(nombre_m, especie_m, edad_m)


# Punto de entrada del programa
if __name__ == "__main__":
    main()