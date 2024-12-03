public class Main {
    public static void main(String[] args) {
        Funcionario f1 = new Funcionario();
        Funcionario f2 = new Funcionario();
        Funcionario f3 = new Funcionario();
        f1.salario = 2000f;
        f2.salario = 4500f;
        f3.salario = 6500f;

        System.out.println(f1.calcularImposto());
        System.out.println(f2.calcularImposto());
        System.out.println(f3.calcularImposto());
    }
}
