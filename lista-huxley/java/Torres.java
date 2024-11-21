import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Torres {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();

        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < n; i++) {
            int value = scanner.nextInt();
            map.put(value, map.getOrDefault(value, 0) + 1);
        }

        int qtd_torres = map.size();
        int torre_maior = 0;

        for (int value : map.values()) {
            if (value > torre_maior) {
                torre_maior = value;
            }
        }
        System.out.printf("%d %d", torre_maior, qtd_torres);
        scanner.close();
    }
}
