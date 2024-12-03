class Funcionario {
    String nome;
    String cpf;
    Float salario;

    public Float calcularImposto(){
        if(salario < 2000){
            return salario;
        }

        if(salario < 5000){
            return salario * 0.9f;
        }

        return salario * 0.8f;
    }
}