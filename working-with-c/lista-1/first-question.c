#include <stdio.h>

int main(int argc, char const *args[]){
    int entradaMetros;
    printf("Digite um valor em metros: ");
    scanf("%d", &entradaMetros);
    printf("O valor em decimetros é: %d\n", entradaMetros * 10);
    printf("O valor em centimetros é: %d\n", entradaMetros * 100);
    printf("O valor em milimetros é: %d\n", entradaMetros * 1000);
}