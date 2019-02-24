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

	twoCount := 0
	threeCount := 0
	for scanner.Scan() {
		line := scanner.Text()
		hasTwo, hasThree := twoThreeCounts(line)
		if hasTwo {
			twoCount++
		}
		if hasThree {
			threeCount++
		}
	}
	fmt.Println(twoCount * threeCount)
}

func twoThreeCounts(id string) (bool, bool) {
	letterCounts := make(map[byte]int)
	for i := 0; i < len(id); i++ {
		letter := id[i]
		letterCounts[letter] = letterCounts[letter] + 1
	}
	hasTwo := hasCount(letterCounts, 2)
	hasThree := hasCount(letterCounts, 3)
	return hasTwo, hasThree
}

func hasCount(letterCounts map[byte]int, count int) bool {
	for _, val := range letterCounts {
		if val == count {
			return true
		}
	}
	return false
}
