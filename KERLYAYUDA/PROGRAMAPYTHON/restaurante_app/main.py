from producto import Producto
from cliente import Cliente
from restaurante import Restaurante

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