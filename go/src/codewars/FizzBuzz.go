package codewars

import (
	"fmt"
)

func Fizzbuzz() {
	for i := 1; i < 101; i++ {
		switch {
		case i%3 == 0 && i%5 == 0:
			fmt.Println("FizzBuzz")
			break
		case i%3 == 0:
			fmt.Println("Fizz")
			break
		case i%5 == 0:
			fmt.Println("Buzz")
			break
		default:
			fmt.Println(i)
			break
		}
	}
}
