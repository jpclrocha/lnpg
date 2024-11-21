import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Scanner;
import java.util.Set;

public class Uniao {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int qtd_1, qtd_2;

        qtd_1 = scanner.nextInt();
        scanner.nextLine();
        qtd_2 = scanner.nextInt();

        List<String> list_1 = new ArrayList<>();
        List<String> list_2 = new ArrayList<>();

        System.out.println("Valores do 1");
        for (int i = 0; i < qtd_1; i++) {
            list_1.add(scanner.next());
        }

        System.out.println("Valores do 2");
        for (int i = 0; i < qtd_2; i++) {
            list_2.add(scanner.next());
        }

        Set<String> uniao = new HashSet<>();
        uniao.addAll(list_1);
        uniao.addAll(list_2);
        

        
        System.out.println(uniao.toString());

        scanner.close();
    }
}
