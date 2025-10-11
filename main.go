package main

import (
	"fmt"
	"runtime"
	"trin/ejercicios"
	"trin/teclado"
	"trin/variables"
)

func main() {
	fmt.Println("Hola Mundo")

	variables.MuestroEnteros()

	variables.RestoVariables()

	variables.ConviertoATexto(15988)

	estado, texto := variables.ConviertoATexto(468464)
	fmt.Println(estado)
	fmt.Println(texto)

	// O debe cambiarse por Darwin.
	if os := runtime.GOOS; os == "linux" || os == "OS X" {
		fmt.Println("Esto no es Windows")
	} else {
		fmt.Println("Esto es Windows")
	}

	switch os := runtime.GOOS; os {
	case "linux":
		fmt.Println("Esto es Linux")
	case "darwin":
		fmt.Println("Esto es Darwin")

	default:
		fmt.Printf("%s \n", os)
	}

	numero, texto := ejercicios.ConvNumerico("50")
	fmt.Println(numero)
	fmt.Println(texto)

	teclado.IngresosNumeros()
}
