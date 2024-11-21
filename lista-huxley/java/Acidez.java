import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Acidez {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double temp = 0;

        List<Double> inputs = new ArrayList<>();

        while (temp != -1) {
            temp = scanner.nextDouble();
            if(temp != -1){
                inputs.add(temp);
            }
        }

        for (Double value : inputs) {
            if (value == 7.0) {
                System.out.println("NEUTRA");
            } else if (value < 7.0) {
                System.out.println("ACIDA");
            } else {
                System.out.println("BASICA");
            }
        }
        scanner.close();
    }
}