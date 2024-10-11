#include <stdio.h>

/*
O cardápio de uma lanchonete é dado abaixo. Prepare um algoritmo que leia a quantidade
de cada item que você consumiu e calcule a conta final.

Hambúrguer................. R$ 3,00
Cheeseburger.............. R$ 2,50
Fritas........................... R$ 2,50
Refrigerante................. R$ 1,00
*/
int main(int argsc, char const *args[]){
    printf("Cardapio\n");
    printf("Hamburguer................. R$ 3,00\n");
    printf("Cheeseburger.............. R$ 2,50\n");
    printf("Fritas........................... R$ 2,50\n");
    printf("Refrigerante................. R$ 1,00\n");
    
    int h, c, f ,r;

    printf("Quantos hambugers voce comeu? ");
    scanf("%d", &h);

    printf("Quantos cheeseburgers voce comeu? ");
    scanf("%d", &c);

    printf("Quantas fritas voce comeu? ");
    scanf("%d", &f);

    printf("Quantos refrigerantes voce tomou? ");
    scanf("%d", &r);

    printf("A conta total eh: %f", 3 * h + 2.5 * c + 2.5 * f + 1 * r);
}

