package iteraciones

import "fmt"

func Iterar() {

	i := 0
	for i < 10 {
		fmt.Println(i)
		i++
	}

}

func Iterar2() {

	// for i := 0; i < 100; i -= 5 {
	for i := 0; i < 100; i += 5 {
		fmt.Println(i)
	}
}

func Iterar3() {

	for i := 10; i > 1; i-- {
		if i == 6 {
			continue
		}
		fmt.Println(i)
	}
}
