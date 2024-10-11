#include <stdio.h>

int main(int argc, char const *args[]){
    float n1,n2,n3;
    printf("Digite a primeira nota: ");
    scanf("%f", &n1);

    printf("Digite a segunda nota: ");
    scanf("%f", &n2);

    printf("Digite a terceira nota: ");
    scanf("%f", &n3);

    float media = (n1 + n2 + n3) / 3;
    
    printf("Media das notas: %.2f\n", media);
}