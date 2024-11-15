package main

import "fmt"

// Leia 2 valores: X e Y. A seguir, calcule e mostre a soma dos números impares entre eles.
func Q4() {
	var x, y int

	fmt.Printf("Digite o primeiro numero: ")
	fmt.Scanf("%d", &x)

	fmt.Printf("Digite o segundo numero: ")
	fmt.Scanf("%d", &y)

	fmt.Printf("Numeros impares entre %d e %d\n", x, y)
	if x < y {
		for i := x; i < y; i++ {
			if i%2 != 0 {
				fmt.Println(i)
			}
		}
	} else if x > y {
		for i := y; i < x; i++ {
			if i%2 != 0 {
				fmt.Println(i)
			}
		}
	} else {
		fmt.Println("Nao existem numeros inteiros impares entre eles porque eles sao iguais")
	}

}
