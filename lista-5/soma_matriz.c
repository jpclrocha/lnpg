#include <stdio.h>

int main(){
    int m,n;

    printf("Digite o valor M de linhas: ");
    scanf("%d", &m);

    printf("Digite o valor n de colunas: ");
    scanf("%d", &n);

    int primeira_matriz[m][n];
    int segunda_matriz[m][n];


    printf("\nValores da primeira matriz\n");
    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < n; j++)
        {
            printf("Digite o valor da linha %d coluna %d: ", i, j);
            scanf("%d", &primeira_matriz[i][j]);
        }
        
    }

    printf("\nValores da segunda matriz\n");
    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < n; j++)
        {
            printf("Digite o valor da linha %d coluna %d: ", i, j);
            scanf("%d", &segunda_matriz[i][j]);
        }
        
    }
    
    printf("\nSoma das matrizes\n");
    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < n; j++)
        {
            printf("Linha %d Coluna %d %d\n",i,j,primeira_matriz[i][j] + segunda_matriz[i][j]);
        }
    }
}