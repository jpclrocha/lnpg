package main

import "fmt"

func main() {
	var total int
	fmt.Print("Digite o valor a sacar: ")
	fmt.Scan(&total)
	qtd_200, qtd_100, qtd_50, qtd_20, qtd_10, qtd_5, qtd_2, qtd_1 := 0, 0, 0, 0, 0, 0, 0, 0
	if total >= 200 {
		resto := total % 200
		qtd_200 = (total - resto) / 200
		total = resto
	}

	if total >= 100 {
		resto := total % 100
		qtd_100 = (total - resto) / 100
		total = resto
	}

	if total >= 50 {
		resto := total % 50
		qtd_50 = (total - resto) / 50
		total = resto
	}

	if total >= 20 {
		resto := total % 20
		qtd_20 = (total - resto) / 20
		total = resto
	}

	if total >= 10 {
		resto := total % 10
		qtd_10 = (total - resto) / 10
		total = resto
	}

	if total >= 5 {
		resto := total % 5
		qtd_5 = (total - resto) / 5
		total = resto
	}

	if total >= 2 {
		resto := total % 2
		qtd_2 = (total - resto) / 2
		total = resto
	}

	if total >= 1 {
		resto := total % 1
		qtd_1 = (total - resto) / 1
		total = resto
	}

	if qtd_200 > 0 {
		fmt.Printf("Notas de 200: %d\n", qtd_200)
	}
	if qtd_100 > 0 {
		fmt.Printf("Notas de 100: %d\n", qtd_100)
	}
	if qtd_50 > 0 {
		fmt.Printf("Notas de 50: %d\n", qtd_50)
	}
	if qtd_20 > 0 {
		fmt.Printf("Notas de 20: %d\n", qtd_20)
	}
	if qtd_10 > 0 {
		fmt.Printf("Notas de 10: %d\n", qtd_10)
	}
	if qtd_5 > 0 {
		fmt.Printf("Notas de 5: %d\n", qtd_5)
	}
	if qtd_2 > 0 {
		fmt.Printf("Notas de 2: %d\n", qtd_2)
	}
	if qtd_1 > 0 {
		fmt.Printf("Notas de 1: %d\n", qtd_1)
	}
}
