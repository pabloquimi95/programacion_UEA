package Semana13;

import java.util.Scanner;

public class semana13 {
    
    // 1. Declaración del método
    // 2. Recibe dos parámetros: pago por hora y horas trabajadas
    public static double calcularSalarioSemanal(double pagoPorHora, int horasTrabajadas) {
        // 3. Realiza el cálculo
        double salarioTotal = pagoPorHora * horasTrabajadas;
        
        // 4. Retorna el resultado
        return salarioTotal;
    }

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        
        System.out.println("--- Sistema de Nómina ---");
        
        // Entrada de datos
        System.out.print("Ingrese el pago por hora: ");
        double precioHora = entrada.nextDouble();
        
        System.out.print("Ingrese las horas trabajadas en la semana: ");
        int horas = entrada.nextInt();
        
        // 5. Llamada al método desde el main y mostrar resultado
        double resultado = calcularSalarioSemanal(precioHora, horas);
        
        System.out.println("-------------------------");
        System.out.println("El salario total es: $" + resultado);
    }
}

