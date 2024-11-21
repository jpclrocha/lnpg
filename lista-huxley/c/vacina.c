#include <stdio.h>

void main()
{
    int ano, periodicidade;
    scanf("%d", &ano);
    scanf("%d", &periodicidade);

    printf("%d %d %d", ano + periodicidade, ano + periodicidade * 2, ano + periodicidade * 3);
}