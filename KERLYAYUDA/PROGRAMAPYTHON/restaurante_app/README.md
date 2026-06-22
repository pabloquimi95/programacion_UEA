Sistema de Gestión de Restaurante (Python)

Proyecto desarrollado en **Python** utilizando **Programación Orientada a Objetos (POO)**.  
Simula la gestión básica de un restaurante, permitiendo manejar productos, clientes y pedidos.

---

## 📌 Características

- Gestión de productos del menú
- Activación y desactivación de productos
- Registro de clientes
- Asociación de pedidos a clientes
- Cálculo del total a pagar
- Código organizado en múltiples archivos (buenas prácticas)

---

## 🧱 Estructura del Proyecto
restaurante_app/
├── modelos/
│   ├── producto.py      # Define la entidad Producto
│   └── cliente.py       # Define la entidad Cliente y sus métodos de consumo
├── servicios/
│   └── restaurante.py   # Clase Restaurante (Lógica central del negocio)
└── main.py              # Punto de arranque exclusivo y simulación del sistema
README.md                # Documentación obligatoria del proyecto