package main

import "fmt"

func soma(a int, b int) (int, int) {
	maior := a
	if b > a {
		maior = b
	}
	return a + b, maior
}

func main() {
	soma, maior := soma(10, 20)
	fmt.Printf("Soma: %d\n", soma)
	fmt.Printf("Maior: %d\n", maior)
}
