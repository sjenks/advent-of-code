package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

func main() {
	frequency := 0
	seen := make(map[int]bool)
	for {
		file, err := os.Open("input.txt")
		if err != nil {
			log.Fatal(err)
		}
		defer file.Close()
		scanner := bufio.NewScanner(file)

		for scanner.Scan() {
			freq, _ := strconv.Atoi(scanner.Text())
			frequency += freq
			if seen[frequency] {
				fmt.Println("seen", frequency)
				return
			}
			seen[frequency] = true
		}
	}

	// fmt.Println(frequency)
}
