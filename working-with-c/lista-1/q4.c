#include <stdio.h>

int main(int argc, char const *args[]){
    float n1,n2,n3;
    float p1,p2,p3;

    printf("Digite a primeira nota: ");
    scanf("%f", &n1);
    printf("Digite o primeiro peso: ");
    scanf("%f", &p1);

    printf("Digite a segunda nota: ");
    scanf("%f", &n2);
    printf("Digite o segundo peso: ");
    scanf("%f", &p2);

    printf("Digite a terceira nota: ");
    scanf("%f", &n3);
    printf("Digite o terceiro peso: ");
    scanf("%f", &p3);

    float media = ((n1 * p1) + (n2 * p2) + (n3 * p3)) / (p1 + p2 + p3);
    
    printf("Media das notas: %.2f\n", media);
}