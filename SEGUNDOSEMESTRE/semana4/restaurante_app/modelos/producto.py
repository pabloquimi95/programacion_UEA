class Producto:
    def __init__(self, nombre: str, precio: float, tipo: str):
        """Representa un producto, plato o bebida del restaurante."""
        self.nombre = nombre
        self.precio = precio
        self.tipo = tipo  # Ejemplo: 'Plato Fuerte', 'Bebida'

    def __str__(self):
        """Método especial para retornar la representación en texto del producto."""
        return f"{self.nombre} ({self.tipo}) - ${self.precio:.2f}"