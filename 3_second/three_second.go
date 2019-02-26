package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

func main() {
	file, err := os.Open("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()
	scanner := bufio.NewScanner(file)

	fabricSize := 1000
	ownership := make([][]int, fabricSize, fabricSize)
	for i := 0; i < fabricSize; i++ {
		ownership[i] = make([]int, fabricSize, fabricSize)
	}

	ownershipPtr := &ownership
	var inputLines []string
	for scanner.Scan() {
		line := scanner.Text()
		inputLines = append(inputLines, line)
	}

	for _, line := range inputLines {
		xCoord, yCoord := parseForLocation(line)
		xSize, ySize := parseForSize(line)
		mark(ownershipPtr, xCoord, yCoord, xSize, ySize)
	}

	multipleClaims := 0
	for x := 0; x < len(ownership); x++ {
		for y := 0; y < len(ownership[x]); y++ {
			if ownership[x][y] > 1 {
				multipleClaims++
			}
		}
	}

	for _, line := range inputLines {
		xCoord, yCoord := parseForLocation(line)
		xSize, ySize := parseForSize(line)
		claim := parseForClaim(line)

		if !ownershipConflict(ownershipPtr, xCoord, yCoord, xSize, ySize) {
			fmt.Println("conflict free at", claim)
		}
	}
}

func parseForClaim(in string) string {
	fullSplit := strings.Split(in, " ")
	return fullSplit[0]
}

func parseForLocation(in string) (int, int) {
	fullSplit := strings.Split(in, " ")
	locStr := fullSplit[2]
	locSplit := strings.Split(locStr, ",")
	xCoord, _ := strconv.Atoi(locSplit[0])
	yCoord, _ := strconv.Atoi(locSplit[1])
	return xCoord, yCoord
}

func parseForSize(in string) (int, int) {
	fullSplit := strings.Split(in, " ")
	lenStr := fullSplit[3]
	lenSplit := strings.Split(lenStr, "x")
	xLen, _ := strconv.Atoi(lenSplit[0])
	yLen, _ := strconv.Atoi(lenSplit[1])
	return xLen, yLen
}

func mark(ownershipPtr *[][]int, xCoord int, yCoord int, xLen int, yLen int) {
	var ownership [][]int
	ownership = *ownershipPtr
	for x := xCoord; x < (xCoord + xLen); x++ {
		for y := yCoord; y < (yCoord + yLen); y++ {
			ownership[x][y] = ownership[x][y] + 1
		}
	}
}

func ownershipConflict(ownershipPtr *[][]int, xCoord int, yCoord int, xLen int, yLen int) bool {
	var ownership [][]int
	ownership = *ownershipPtr

	for x := xCoord; x < (xCoord + xLen); x++ {
		for y := yCoord; y < (yCoord + yLen); y++ {
			if ownership[x][y] > 1 {
				//fmt.Print(ownership[x][y])
				return true
			}
		}
		//fmt.Println("")
	}
	return false
}
