#include <stdio.h>

// Faça um algoritmo para ler um número que é um código de usuário. Caso este código seja
// diferente de um código armazenado internamente no algoritmo (igual a 1234) deve ser
// apresentada a mensagem ‘Usuário inválido!’. Caso o Código seja correto, deve ser lido outro
// valor que é a senha. Se esta senha estiver incorreta (a certa é 9999) deve ser mostrada a
// mensagem ‘senha incorreta’. Caso a senha esteja correta, deve ser mostrada a mensagem
// ‘Acesso permitido’.

void main(){
    int cod_user = 1234;
    int senha = 9999;

    int cod_input, senha_input;

    printf("Digite o codigo de usuario: ");
    scanf("%d", &cod_input);

    while(cod_input != cod_user){
        printf("Usuário inválido!\n");
        printf("Digite o codigo de usuario: ");
        scanf("%d", &cod_input);
    }

    printf("Digite a senha: ");
    scanf("%d", &senha_input);
    while(senha_input != senha){
        printf("Senha incorreta\n");
        printf("Digite a senha: ");
        scanf("%d", &senha_input);
    }

    printf("Acesso permitido");
}