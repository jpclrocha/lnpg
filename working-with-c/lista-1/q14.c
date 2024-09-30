#include <stdio.h>

/* 14) Escreva um algoritmo para ler o salário mensal atual de um funcionário e o percentual de
reajuste. Calcular e escrever o valor do novo salário.
*/

int main(int argc, char const *args[]){
    float salario, reajuste;

    printf("Digite o salario do funcionario: ");
    scanf("%f", &salario);

    printf("Digite o percentual de reajuste do salario: ");
    scanf("%f", &reajuste);

    printf("O novo salario do funcionario sera: %f", salario * (1 + reajuste / 100));
}