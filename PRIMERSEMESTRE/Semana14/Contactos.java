import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Contactos {

    public static void main(String[] args) {

        // Creación de la colección (diccionario)
        Map<String, String> contactos = new HashMap<>();
        Scanner scanner = new Scanner(System.in);
        int opcion;

        do {
            System.out.println("\n--- AGENDA DE CONTACTOS ---");
            System.out.println("1. Agregar contacto");
            System.out.println("2. Mostrar contactos");
            System.out.println("3. Buscar contacto");
            System.out.println("4. Eliminar contacto");
            System.out.println("5. Salir");
            System.out.print("Seleccione una opción: ");
            opcion = scanner.nextInt();
            scanner.nextLine(); // limpiar buffer

            switch (opcion) {
                case 1:
                    System.out.print("Ingrese el nombre: ");
                    String nombre = scanner.nextLine();
                    System.out.print("Ingrese el número telefónico: ");
                    String telefono = scanner.nextLine();
                    contactos.put(nombre, telefono);
                    System.out.println("Contacto agregado correctamente.");
                    break;

                case 2:
                    System.out.println("\nLista de contactos:");
                    for (Map.Entry<String, String> entry : contactos.entrySet()) {
                        System.out.println("Nombre: " + entry.getKey() + 
                                           " - Teléfono: " + entry.getValue());
                    }
                    break;

                case 3:
                    System.out.print("Ingrese el nombre a buscar: ");
                    String buscar = scanner.nextLine();
                    if (contactos.containsKey(buscar)) {
                        System.out.println("Teléfono: " + contactos.get(buscar));
                    } else {
                        System.out.println("Contacto no encontrado.");
                    }
                    break;

                case 4:
                    System.out.print("Ingrese el nombre a eliminar: ");
                    String eliminar = scanner.nextLine();
                    if (contactos.remove(eliminar) != null) {
                        System.out.println("Contacto eliminado.");
                    } else {
                        System.out.println("El contacto no existe.");
                    }
                    break;

                case 5:
                    System.out.println("Programa finalizado.");
                    break;

                default:
                    System.out.println("Opción inválida.");
            }

        } while (opcion != 5);

        scanner.close();
    }
}