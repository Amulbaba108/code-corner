package main

import (
	"fmt"
	"strings"
)

var numerals = []struct {
	value  int
	symbol string
}{
	{1000, "M"}, {500, "D"}, {100, "C"}, {50, "L"}, {10, "X"}, {5, "V"}, {1, "I"},
}

func main() {
	var n int
	fmt.Scan(&n)
	var out strings.Builder
	for _, r := range numerals {
		for n >= r.value {
			out.WriteString(r.symbol)
			n -= r.value
		}
	}
	fmt.Println(out.String())
}
