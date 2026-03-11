public static void main(String[] args) {
     Scanner leer = new Scanner(System.in);

    int[][] asientos = new int[3][4];
    int f, c;

    System.out.println("Ingrese fila (0 a 2): ");
    f = leer.nextInt();

    System.out.println("Ingrese columna (0 a 3): ");
    c = leer.nextInt();

    asientos[f][c] = 1;

    System.out.println("Estado de la sala:");

    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 4; j++) {
            System.out.print(asientos[i][j] + " ");
        }
        System.out.println();
    }
}