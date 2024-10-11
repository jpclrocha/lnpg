#include <stdio.h>

/*
13) Escreva um algoritmo para ler o número total de eleitores de um município, o número de
votos brancos, nulos e válidos. Calcular e escrever o percentual que cada um representa em
relação ao total de eleitores.
*/

int main(int argc, char const *args[]){
    int eleitores, brancos, nulos, validos;

    printf("Digite a quantidade de eleitores: ");
    scanf("%d", &eleitores);

    printf("Digite a quantidade de votos brancos: ");
    scanf("%d", &brancos);

    printf("Digite a quantidade de votos nulos: ");
    scanf("%d", &nulos);

    printf("Digite a quantidade de votos validos: ");
    scanf("%d", &validos);

    printf("Porcentagem de votos brancos: %.2f%%\n", (float) brancos / eleitores * 100.0);
    printf("Porcentagem de votos nulos: %.2f%%\n", (float) nulos / eleitores * 100.0);
    printf("Porcentagem de votos validos: %.2f%%\n", (float) validos / eleitores * 100.0);
}