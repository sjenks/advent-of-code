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

	timeAsleep := make(map[string][]int)
	timeWentToSleep := -1
	currentGuard := "-1"

	for _, action := range sortedActions {
		currentTime := action.time.Minute()

		if action.verb == "beginsshift" {
			currentGuard = action.guardNumber
		} else if action.verb == "fallsasleep" {
			timeWentToSleep = currentTime
		} else if action.verb == "wakesup" {
			_, exists := timeAsleep[currentGuard]
			if !exists {
				timeAsleep[currentGuard] = make([]int, 60, 60)
			}

			for i := timeWentToSleep; i < currentTime; i++ {
				timeAsleep[currentGuard][i] = timeAsleep[currentGuard][i] + 1
			}
			timeWentToSleep = -1
		} else {
			fmt.Println("herp derp - unknown verb", action.verb)
		}
	}

	maxAsleepCount := 0
	sleepiestGuard := "-1"
	sleepiestTime := -1
	for guardNum, timeSlice := range timeAsleep {
		for time, sleepCount := range timeSlice {
			if sleepCount > maxAsleepCount {
				maxAsleepCount = sleepCount
				sleepiestTime = time
				sleepiestGuard = guardNum
			}
		}
	}
	fmt.Println("max sleep count", maxAsleepCount, "sleepiest time", sleepiestTime, "sleepiest guard", sleepiestGuard)
}
