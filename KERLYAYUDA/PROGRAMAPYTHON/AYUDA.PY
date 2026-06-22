class Producto:
    def _init_(self, codigo, nombre, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.activo = True

    def desactivar_producto(self):
        self.activo = False

    def mostrar(self):
        if self.activo:
            estado = "Disponible"
        else:
            estado = "Agotado"

        print(f"Código: {self.codigo} | {self.nombre} | ${self.precio:.2f} | {estado}")


class Cliente:
    def _init_(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono
        self.pedidos = []

    def agregar_pedido(self, producto):
        self.pedidos.append(producto)

    def mostrar_pedido(self):
        print(f"\nPedido de {self.nombre}:")
        total = 0

        for producto in self.pedidos:
            print(f"- {producto.nombre}: ${producto.precio:.2f}")
            total += producto.precio

        print(f"Total a pagar: ${total:.2f}")


class Restaurante:
    def _init_(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion
        self.menu = []
        self.clientes = []

    def agregar_al_menu(self, producto):
        self.menu.append(producto)

    def registrar_cliente(self, cliente):
        self.clientes.append(cliente)

    def mostrar_menu(self):
        print("\n--- MENÚ DEL RESTAURANTE ---")
        for producto in self.menu:
            producto.mostrar()

    def mostrar_clientes(self):
        print("\n--- CLIENTES REGISTRADOS ---")
        for cliente in self.clientes:
            print(f"{cliente.nombre} - Teléfono: {cliente.telefono}")


# Programa principal

restaurante = Restaurante("El Rincón del Sabor", "Guayaquil")

hamburguesa = Producto(1, "Hamburguesa clásica", 3.50)
pizza = Producto(2, "Pizza personal", 4.00)
limonada = Producto(3, "Limonada", 1.25)
papas = Producto(4, "Papas fritas", 2.00)

restaurante.agregar_al_menu(hamburguesa)
restaurante.agregar_al_menu(pizza)
restaurante.agregar_al_menu(limonada)
restaurante.agregar_al_menu(papas)

cliente1 = Cliente("María López", "0987654321")
cliente2 = Cliente("José Andrade", "0998765432")

restaurante.registrar_cliente(cliente1)
restaurante.registrar_cliente(cliente2)

cliente1.agregar_pedido(hamburguesa)
cliente1.agregar_pedido(limonada)

cliente2.agregar_pedido(pizza)
cliente2.agregar_pedido(papas)

papas.desactivar_producto()

print("RESTAURANTE:", restaurante.nombre)
print("DIRECCIÓN:", restaurante.direccion)

restaurante.mostrar_menu()
restaurante.mostrar_clientes()

cliente1.mostrar_pedido()
cliente2.mostrar_pedido()