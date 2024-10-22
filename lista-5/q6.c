#include <stdio.h>
// Apresente todos os números divisíveis por 5 que sejam maiores do que 0 e menores ou
// iguais a 200.

int main(){
    for(int i = 0; i <=200; i++) {
        if(i % 5 == 0 && i > 0){
            printf("%d\n" ,i);
        }
    }
}