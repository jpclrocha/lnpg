import java.util.Scanner;

public class Zerinho {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int a, b, c;

        a = scanner.nextInt();
        b = scanner.nextInt();
        c = scanner.nextInt();

        if((a == 1 && b == 0 && c == 0) || (a == 0 && b == 1 && c == 1)){
            System.out.println("A");
        }else if((a == 0 && b == 1 && c == 0) || (a == 1 && b == 0 && c == 1)){
            System.out.println("B");
        }else if((a == 0 && b == 0 && c == 1) || a == 1 && b == 1 && c == 0){
            System.out.println("C");
        }else{
            System.out.println("*");
        }

        scanner.close();
    }
}
