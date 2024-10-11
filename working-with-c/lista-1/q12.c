#include <stdio.h>
/*
12) Faça um algoritmo que calcule a área e o perímetro de um retângulo. As entradas do
programa serão a largura e a altura do triângulo.
*/

int main(int argc, char const *args[]){
    float h, l;

    printf("Digite a largura do retangulo: ");
    scanf("%f", &l);

    printf("Digite a altura do retangulo: ");
    scanf("%f", &h);

    printf("A area do retangulo eh: %f", h * l);
    printf("O perimetro do retangulo eh: %f", 2 * h + 2 * l);
}