from servicios.restaurante import Restaurante
from modelos.producto import Producto
from modelos.cliente import Cliente

def iniciar_demostracion():
    # 1. Instanciar el servicio principal
    app_restaurante = Restaurante("QXpertech Gourmet")

    print("--- PASO 1: CARGANDO PRODUCTOS AL MENÚ ---")
    # 2. Instanciar productos
    plato1 = Producto("Encebollado Completo", 4.50, "Plato Fuerte")
    plato2 = Producto("Seco de Carne", 4.50, "Plato Fuerte")
    bebida1 = Producto("Jugo de Guayaba", 1.25, "Bebida")
    porcion1 = Producto("Porción de Chifles", 0.75, "Extra")

    # Guardar productos en el restaurante
    app_restaurante.agregar_al_menu(plato1)
    app_restaurante.agregar_al_menu(plato2)
    app_restaurante.agregar_al_menu(bebida1)
    app_restaurante.agregar_al_menu(porcion1)

    # Mostrar catálogo
    app_restaurante.mostrar_menu_disponible()

    print("\n--- PASO 2: REGISTRO DE CLIENTE Y PEDIDOS ---")
    # 3. Instanciar un cliente
    cliente_actual = Cliente("Pablo Sergio Quimi Pin", "0999999999")
    app_restaurante.registrar_cliente(cliente_actual)

    # Simular la selección de productos usando los objetos directamente
    cliente_actual.ordenar_producto(plato1)     # Ordena Encebollado
    cliente_actual.ordenar_producto(porcion1)   # Ordena Chifles
    cliente_actual.ordenar_producto(bebida1)    # Ordena Jugo
    print(f"\n[Acción] {cliente_actual.nombre} ha seleccionado sus productos.")

    print("\n--- PASO 3: DEMOSTRACIÓN DE COMUNICACIÓN ENTRE MÓDULOS ---")
    # 4. El restaurante procesa la cuenta interactuando con el objeto cliente
    app_restaurante.procesar_pago(cliente_actual)


if __name__ == "__main__":
    iniciar_demostracion()