#include <stdio.h>

// Ler 3 valores (A, B e C) representando as medidas dos lados de um triângulo e escrever se
// formam ou não um triângulo. OBS: para formar um triângulo, o valor de cada lado deve ser
// menor que a soma dos outros 2 lados.

void main() {
	int a, b, c;

	printf("Digite o tamanho do lado A: ");
	scanf("%d", &a);
	printf("Digite o tamanho do lado B: ");
	scanf("%d", &b);
	printf("Digite o tamanho do lado C: ");
	scanf("%d", &c);

	if(a + b < c){
		printf("Um triangulo nao pode ser formado");
	}else if (a + c < b)
	{
		printf("Um triangulo nao pode ser formado");
	}else if(b + c < a){
		printf("Um triangulo nao pode ser formado");
	}else{
		printf("Um triangulo pode ser formado");
	}
	
}
