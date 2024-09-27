#include <stdio.h>
#include <math.h>

int main(int argc, char const *args[]){
    float input;

    printf("Digite uma temperatura em graus celsius: ");
    scanf("%f", &input);

    float celsius = 5 * (input - 32) / 9;
    
    printf("%.2f convertido para Celsius: %.2f\n", input, celsius);
}