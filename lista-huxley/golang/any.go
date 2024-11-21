package main

import "fmt"

func Any() {
	value := 0

	values := make([]int, 0)

	for value != -1 {
		fmt.Print("Digite o numero do PH: ")
		fmt.Scanf("%d", &value)
		if value == -1 {
			values = append(values, value)
		}
	}

	for i := 0; i < len(values); i++ {
		if values[i] < 7 {
			fmt.Printf("Valor %d eh acido\n", i)
		}

		if values[i] == 7 {
			fmt.Printf("Valor %d eh neutro\n", i)
		}

		if values[i] > 7 {
			fmt.Printf("Valor %d eh basico\n", i)
		}
	}
}
