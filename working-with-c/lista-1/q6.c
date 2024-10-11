#include <stdio.h>

int main(int argc, char const *args[]){
    int input;

    printf("Digite um valor representando um numero de segundos: ");
    scanf("%d", &input);

    int horas = input / 60 / 60;
    int minutos = (input / 60) - horas * 60;
    int segundos = input - ((horas * 60 + minutos) * 60);
    
    printf("%d segundos sao %d hora (s), %d minuto (s) e %d segundo (s)\n", input, horas, minutos, segundos);
}