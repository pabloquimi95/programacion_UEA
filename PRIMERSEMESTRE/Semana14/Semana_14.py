def calcular_area(base, altura):
    # Proceso: Multiplicación de los datos recibidos
    resultado_area = base * altura
    # Retorno: Envía el valor calculado de vuelta al programa principal
    return resultado_area

# --- Bloque Principal ---
b = float(input("Ingrese la base: "))
h = float(input("Ingrese la altura: "))

# Llamada a la función con argumentos
area_final = calcular_area(b, h)

print(f"El área total es: {area_final}")