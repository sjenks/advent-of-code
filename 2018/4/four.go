package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"sort"
	"strings"
	"time"
)

func main() {
	allActions := readAllActions()
	sort.Sort(allActions)
	findSleeper(allActions)
}

func readAllActions() actionSlice {
	file, err := os.Open("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()
	scanner := bufio.NewScanner(file)

	var allActions actionSlice
	allActions = make([]actionData, 0)
	for scanner.Scan() {
		line := scanner.Text()
		// The input file is kinda a pain for this one
		fullSplit := strings.Split(line, ",") // {[1518-03-19 00:02]} {Guard #647 begins shift}

		guardString := fullSplit[1] // "Guard #647 begins shift"

		guardSplit := strings.Split(guardString, " ") //{Guard} {#647} {begins} {shift}

		var actionStr string
		guardNum := ""
		if len(guardSplit) == 4 {
			guardNum = guardSplit[1]
			actionStr = guardSplit[2] + guardSplit[3] // intentionally remove space
		} else {
			actionStr = guardSplit[0] + guardSplit[1]
		}

		// fmt.Println(fullSplit[0], lastSeenGuardNumber, actionStr)
		parsedDate, _ := time.Parse("[2006-01-02 15:04]", fullSplit[0])
		data := actionData{verb: actionStr, guardNumber: guardNum, time: parsedDate}
		allActions = append(allActions, data)
	}
	return allActions
}

func findSleeper(sortedActions actionSlice) {

	timeAsleep := make(map[string]int)
	timeWentToSleep := -1
	currentGuard := "-1"

	sleepyGuardRange := make([]int, 60, 60)

	for _, action := range sortedActions {
		currentTime := action.time.Minute()

		if action.verb == "beginsshift" {
			currentGuard = action.guardNumber
		} else if action.verb == "fallsasleep" {
			timeWentToSleep = currentTime
		} else if action.verb == "wakesup" {
			if currentGuard == "#401" {
				for i := timeWentToSleep; i < currentTime; i++ {
					sleepyGuardRange[i] = sleepyGuardRange[i] + 1
				}
			}
			timeAsleep[currentGuard] = (currentTime - timeWentToSleep) + timeAsleep[currentGuard]
			timeWentToSleep = -1
		} else {
			fmt.Println("herp derp - unknown verb", action.verb)
		}
	}

	maxAsleep := 0
	maxGuardNum := "-1"
	for key, val := range timeAsleep {
		if val > maxAsleep {
			maxAsleep = val
			maxGuardNum = key
		}
	}

	maxMinAsleep := -1
	maxTimeAsleep := -1
	for key, val := range sleepyGuardRange {
		if val > maxTimeAsleep {
			maxTimeAsleep = val
			maxMinAsleep = key
		}
	}

	fmt.Println(maxGuardNum, maxAsleep)
	fmt.Println("maxMin asleep", maxMinAsleep, "num times asleep min", maxTimeAsleep)
}
