// Ler 3 valores (considere que não serão informados valores iguais) e escrever o maior deles.

import java.util.Scanner;

public class Q3{
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int a, b, c;

        System.out.println("Digite o numero 1: ");
        a = scanner.nextInt();   
        
        System.out.println("Digite o numero 2: ");
        b = scanner.nextInt();  

        System.out.println("Digite o numero 3: ");
        c = scanner.nextInt();  

        if(a > b && a > c) System.out.println("O maior numero eh: " + a);
        if(b > a && b > c) System.out.println("O maior numero eh: " + b);
        if(c > a && c > b) System.out.println("O maior numero eh: " + c);

        scanner.close();
    }
}