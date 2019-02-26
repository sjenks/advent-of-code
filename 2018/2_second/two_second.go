package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
)

func main() {
	file, err := os.Open("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()
	scanner := bufio.NewScanner(file)

	var allBoxes []string
	for scanner.Scan() {
		line := scanner.Text()
		allBoxes = append(allBoxes, line)
	}

	for i := 0; i < len(allBoxes); i++ {
		for j := i + 1; j < len(allBoxes); j++ {
			if diffLetterCount(allBoxes[i], allBoxes[j]) == 1 {
				fmt.Println("Found at:", i, j)
				fmt.Println("Found:", allBoxes[i], "and", allBoxes[j])
			}
		}
	}
}

func diffLetterCount(left string, right string) int {
	diffCount := 0
	for i := 0; i < len(left); i++ {
		if left[i] != right[i] {
			diffCount++
		}
	}
	return diffCount
}
