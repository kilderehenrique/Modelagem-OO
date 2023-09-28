package main

import "fmt"

func main() {

	// INPUT       produto: 0, 1, 2, 3, 4
	qtdsProdutos := [5]int {5, 0, 0, 0, 0}

	precos := [5]float64{0.5, 1, 4, 7, 8}
	compraQtds := [5]int{0, 0, 0, 0, 0}

	// Pega quantidade do INPUT e valida para a SAIDA
	for i := 0; i < 5; i++ {
		// Informa se produto inválido
		if qtdsProdutos[i] < 0 {
			fmt.Println("Produto", (i+1), ": Quantidade inválida!")
		} else {
			// Adiciona produtos a compra
			compraQtds[i] = qtdsProdutos[i]
		}
	}

	// Calcula valor total
	total := 0.0
	for i := 0; i < 5; i++ {
		total += float64(compraQtds[i]) * precos[i]
	}

	fmt.Println("Total: ", total)
}
