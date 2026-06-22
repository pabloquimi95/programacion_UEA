class Cliente:
    def __init__(self, nombre: str, cedula: str):
        """Representa a un cliente del restaurante."""
        self.nombre = nombre
        self.cedula = cedula
        self.productos_consumidos = []  # Lista para almacenar objetos Producto

    def ordenar_producto(self, producto):
        """Agrega un objeto Producto a la lista de consumo del cliente."""
        self.productos_consumidos.append(producto)

    def calcular_total(self) -> float:
        """Calcula de forma automática la sumatoria de los precios consumidos."""
        return sum(prod.precio for prod in self.productos_consumidos)

    def __str__(self):
        """Método especial para representar los datos del cliente."""
        return f"Cliente: {self.nombre} | C.I.: {self.cedula}"