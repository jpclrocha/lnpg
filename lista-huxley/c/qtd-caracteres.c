#include <stdio.h>

// Função para contar o número de caracteres em uma string
int contar_caracteres(char s[])
{
    int contador = 0;
    for (int i = 0; s[i] != '\0'; i++)
    {
        contador++;
    }
    return contador;
}

int main()
{
    char s[51]; // String com espaço para até 50 caracteres + o terminador nulo '\0'
    fgets(s, 51, stdin); // Lê no máximo 50 caracteres, garantindo espaço para '\0'

    // Remove o '\n' no final da string, se existir
    for (int i = 0; s[i] != '\0'; i++)
    {
        if (s[i] == '\n')
        {
            s[i] = '\0';
            break;
        }
    }

    // Verificar se a string não é vazia
    if (s[0] == '\0')
    {
        printf("Erro: A string não pode estar vazia.\n");
        return 1;
    }

    // Chamar a função e exibir o resultado
    int quantidade = contar_caracteres(s);
    printf("%d", quantidade);

    return 0;
}