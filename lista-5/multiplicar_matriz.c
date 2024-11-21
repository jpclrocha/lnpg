#include <stdio.h>

int main()
{
    // onde n é obrigatóriamente o número de colunas da primeira matriz e o numero de linhas da segunda matriz 
    int m, n, p;
    printf("Digite a quantidade de linhas da primeira matriz: ");
    scanf("%d", &m);

    printf("Digite a quantidade de colunas da primeira matriz (tambem sera o numero de linhas da segunda): ");
    scanf("%d", &n);

    printf("Digite a quantidade de colunas da segunda matriz: ");
    scanf("%d", &p);

    signed int matriz_1[m][n], matriz_2[n][p];

    printf("\nValores da primeria matriz\n");
    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < n; j++)
        {
            printf("Digite o valor da linha %d e coluna %d da primeira matriz: ", i, j);
            scanf("%d", &matriz_1[i][j]);
        }
    }

    printf("\nValores da segunda matriz\n");
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < p; j++)
        {
            printf("Digite o valor da linha %d e coluna %d da primeira matriz: ", i, j);
            scanf("%d", &matriz_2[i][j]);
        }
    }

    signed int matriz_resultante[m][p];
    // inicializando a matriz
    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < p; j++)
        {
            matriz_resultante[i][j] = 0;
        }
    }

    printf("\nMultiplicacao das matrizes\n");
    for (int j = 0; j < n; j++)
    {
        for (int i = 0; i < m; i++)
        {
            for (int k = 0; k < p; k++)
            {
                signed int res = matriz_2[j][k] * matriz_1[i][j];
                matriz_resultante[i][k] = res + matriz_resultante[i][k];
            }
        }
    }

    printf("\nValores da matriz resultante:\n");
    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < p; j++)
        {
            printf("Linha %d Coluna %d: %d\n", i, j, matriz_resultante[i][j]);
        }
    }
}