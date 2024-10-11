#include <stdio.h>

/*
11) Uma companhia de carros paga a seus empregados um salário de R$ 500,00 por mês mais
uma comissão de R$ 50,00 para cada carro vendido e mais 5% do valor da venda. Elabore um
algoritmo para calcular e imprimir o salário do vendedor num dado mês recebendo como dados
de entrada o nome do vendedor, o número de carros vendidos e o valor total das vendas.
*/
int main(int argsc, char const *args[]){
    char nome[61];
    int qtd;
    float venda;

    printf("Digite o nome do vendedor: ");
    scanf("%s", nome);

    printf("Quantos carros %s vendeu? ", nome);
    scanf("%d", &qtd);

    printf("Qual o valor total das vendas de %s? ", nome);
    scanf("%f", &venda);

    float salario = 500 + qtd * 50 + 0.05 * venda;

    printf("O salario de %s eh: %f", nome, salario);
}

