#include <stdio.h>

int main() {
    int N, M; 
    scanf("%d %d", &N, &M);

    int tempos[N];
    for (int i = 0; i < N; i++) {
        tempos[i] = 0; // Inicializa o tempo total de cada competidor
        for (int j = 0; j < M; j++) {
            int tempo;
            scanf("%d", &tempo);
            tempos[i] += tempo; // Soma os tempos das voltas
        }
    }

    // Determinar o competidor com o menor tempo
    int vencedor = 0; // Índice do vencedor
    for (int i = 1; i < N; i++) {
        if (tempos[i] < tempos[vencedor]) {
            vencedor = i;
        }
    }

    // Saída: como os competidores são numerados a partir de 1, ajustamos o índice
    printf("%d\n", vencedor + 1);

    return 0;
}
