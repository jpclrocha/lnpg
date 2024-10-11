#include <stdio.h>
#include <math.h>

int main(int argc, char const *args[]){
    int input;

    printf("Digite um numero maior que zero: ");
    scanf("%d", &input);

    while(input < 1){
        printf("Digite um numero maior que zero: ");
        scanf("%d", &input);
    }
    
    printf("%d ao quadrado: %f\n", input, pow(input, 2));
    printf("%d ao cubo: %f\n", input, pow(input, 3));
    printf("Raiz quadrada de %d: %f\n", input, sqrt(input));
    printf("Raiz cubica de %d: %f\n", input, pow(input, 1.0/3.0));
}