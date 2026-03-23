package Semana14;


import java.util.Scanner;

public class TareaFunciones {

    // 1. DEFINICIÓN DE LA FUNCIÓN (MÉTODO)
    // Recibe tres parámetros de tipo double y retorna un double
    public static double calcularPromedio(double n1, double n2, double n3) {
        double suma = n1 + n2 + n3;
        double promedio = suma / 3;
        
        // 2. USO DE RETURN: Envía el resultado fuera de la función
        return promedio;
    }

    public static void main(String[] args) {
        // Preparar el escáner para ingreso por teclado
        Scanner teclado = new Scanner(System.in);

        System.out.println("--- CALCULADORA DE PROMEDIOS ---");

        System.out.print("Ingrese la nota 1: ");
        double nota1 = teclado.nextDouble();

        System.out.print("Ingrese la nota 2: ");
        double nota2 = teclado.nextDouble();

        System.out.print("Ingrese la nota 3: ");
        double nota3 = teclado.nextDouble();

        // 3. LLAMADA A LA FUNCIÓN: Se le pasan los datos capturados
        double resultadoFinal = calcularPromedio(nota1, nota2, nota3);

        // 4. MOSTRAR EL RESULTADO EN PANTALLA
        System.out.println("El promedio final del estudiante es: " + resultadoFinal);
        
        teclado.close();
    }
}