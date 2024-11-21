package main

import "fmt"

func EscadinhaMagica() {
	n := 10

	for i := 1; i <= n; i++ {
		for j := 1; j <= i; j++ {
			fmt.Printf("%d ", j)
		}
		fmt.Printf("\n")
	}
}
