// Construir um algoritmo que leia dois números e efetue a adição. Caso o valor somado seja
// maior que 20, este deverá ser apresentado somando-se a ele mais 8; caso o valor somado seja
// menor ou igual a 20, este deverá ser apresentado subtraindo-se 5.

import java.util.Scanner;

public class Q4 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int a, b;

        System.out.println("Digite o numero 1: ");
        a = scanner.nextInt();   
        
        System.out.println("Digite o numero 2: ");
        b = scanner.nextInt();  

        if(a + b > 20) System.out.println("A soma eh: " + (a + b + 8));
        if(a + b <= 20) System.out.println("A soma eh: " + (a + b - 5));

        scanner.close();
    }
}
