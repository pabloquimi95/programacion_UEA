class Cliente:
    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono
        self.pedidos = []

    def agregar_pedido(self, producto):
        self.pedidos.append(producto)

    def mostrar_pedido(self):
        print(f"\nPedido de {self.nombre}:")
        total = 0
        
        for prod in self.pedidos:
            print(f"- {prod.nombre}: ${prod.precio:.2f}")
            total += prod.precio
            
        print(f"Total a pagar: ${total:.2f}")