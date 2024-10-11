#include <stdio.h>

/*
15) O custo de um carro novo ao consumidor é a soma do custo de fábrica com a porcentagem
do distribuidor e dos impostos (aplicados ao custo de fábrica). Supondo que o percentual do
distribuidor seja de 28% e os impostos de 45%, escrever um algoritmo para ler o custo de
fábrica de um carro, calcular e escrever o custo final ao consumidor.
*/

int main(int argc, char const *args[]){
    float custo;

    printf("Digite o custo de fabrica do carro: ");
    scanf("%f", &custo);

    printf("O custo final eh de: %f", custo * 1.45 * 1.28);
}