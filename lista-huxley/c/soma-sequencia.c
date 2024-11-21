#include <stdio.h>

void main()
{
    int qtd;
    scanf("%d", &qtd);

    int soma = 0;

    for (int i = 0; i < qtd; i++)
    {
        int num = 0;
        scanf("%d", &num);
        soma += num;
    }

    printf("%d", soma);
}