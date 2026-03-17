import java.util.Scanner;

public class SumaDosNumeros {
    public static void main(String[] args) {

        Scanner entrada = new Scanner(System.in);

        System.out.print("Ingrese el primer número: ");
        int num1 = entrada.nextInt();

        System.out.print("Ingrese el segundo número: ");
        int num2 = entrada.nextInt();

        int suma = num1 + num2;

        System.out.println("La suma es: " + suma);

        entrada.close();
    }
}
