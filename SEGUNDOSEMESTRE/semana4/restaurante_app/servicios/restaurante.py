from modelos.producto import Producto
from modelos.cliente import Cliente

class Restaurante:
    def __init__(self, nombre_restaurante: str):
        """Clase que gestiona las operaciones principales del sistema."""
        self.nombre_restaurante = nombre_restaurante
        self.menu = []
        self.clientes = []

    def agregar_al_menu(self, producto: Producto):
        """Permite registrar productos en el menú del restaurante."""
        self.menu.append(producto)
        print(f"[Menú] Producto añadido: {producto.nombre}")

    def registrar_cliente(self, cliente: Cliente):
        """Registra un nuevo cliente en el sistema de atención."""
        self.clientes.append(cliente)
        print(f"[Registro] Cliente registrado: {cliente.nombre}")

    def mostrar_menu_disponible(self):
        """Muestra en pantalla el listado de todos los productos."""
        print(f"\n--- MENÚ DISPONIBLE EN {self.nombre_restaurante.upper()} ---")
        for prod in self.menu:
            print(f" * {prod}")

    def procesar_pago(self, cliente: Cliente):
        """Muestra el detalle final de la cuenta y consumo del cliente."""
        print(f"\n========================================")
        print(f"        CUENTA: {self.nombre_restaurante}")
        print(f"========================================")
        print(cliente)
        print(f"----------------------------------------")
        print("Detalle del consumo:")
        for prod in cliente.productos_consumidos:
            print(f"  - {prod.nombre:<22} ${prod.precio:>6.2f}")
        print(f"----------------------------------------")
        print(f"TOTAL A CANCELAR:         ${cliente.calcular_total():>6.2f}")
        print(f"========================================\n")