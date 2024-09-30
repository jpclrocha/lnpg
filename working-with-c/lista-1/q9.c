#include <stdio.h>

int main(int argc, char const *args[]){
    float p;
    printf("Digite uma quantidade de chuva em polegadas: ");
    scanf("%f", &p);

    printf("%.2f polegadas de chuva eh equivalente a %.2f mm de chuva.\n", p, p * 25.4);
}