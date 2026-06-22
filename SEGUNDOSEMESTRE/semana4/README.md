# Sistema de Gestión de Restaurante - POO en Python

**Estudiante:** Pablo Sergio Quimi Pin  
**Asignatura:** Programación Orientada a Objetos  
**Tarea:** Semana 4 - Organización Modular

---

## 📝 Descripción del Sistema
Este software implementa un sistema básico para la gestión de consumos dentro de un restaurante empleando el paradigma de **Programación Orientada a Objetos (POO)** en Python. El programa permite registrar un catálogo de productos (platos o bebidas) y asociar de forma dinámica el consumo de los mismos a clientes específicos, centralizando el procesamiento de cuentas y facturación a través de un servicio de control.

---

## 📂 Estructura del Proyecto
El repositorio está organizado bajo el siguiente árbol de directorios para respetar los paquetes del software:

```text
restaurante_app/
├── modelos/
│   ├── producto.py      # Define la entidad Producto
│   └── cliente.py       # Define la entidad Cliente y sus métodos de consumo
├── servicios/
│   └── restaurante.py   # Clase Restaurante (Lógica central del negocio)
└── main.py              # Punto de arranque exclusivo y simulación del sistema
README.md                # Documentación obligatoria del proyecto
```
## Reflexión
La modularización y la separación de responsabilidades son fundamentales en el desarrollo de software moderno por las siguientes razones:

Mantenibilidad: Separar los datos puros (modelos) del control operativo (servicios) permite que si en el futuro se requiere cambiar la lógica de facturación o impuestos, solo se altere el archivo del servicio, dejando intacta la estructura de los productos o clientes.

Legibilidad: Al mantener un punto de arranque limpio en main.py libre de lógica de negocio mezclada, cualquier desarrollador externo puede comprender el flujo y funcionamiento del programa a simple vista.

Reutilización: Las clases de los modelos quedan completamente desacopladas, lo que facilitaría utilizarlas en el futuro en otros sistemas o interfaces (como entornos web o móviles) sin reescribir código.