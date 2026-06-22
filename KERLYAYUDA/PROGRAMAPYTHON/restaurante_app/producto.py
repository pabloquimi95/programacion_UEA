class Producto:
    def __init__(self, codigo, nombre, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.activo = True

    def desactivar_producto(self):
        self.activo = False

    def mostrar(self):
        estado = "Disponible" if self.activo else "Agotado"
        print(f"Código: {self.codigo} | {self.nombre} | ${self.precio:.2f} | {estado}")