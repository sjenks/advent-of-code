package main

import (
	"time"
)

type actionData struct {
	verb        string
	time        time.Time
	guardNumber string
}

type actionSlice []actionData

func (p actionSlice) Len() int {
	return len(p)
}

func (p actionSlice) Less(i, j int) bool {
	return p[i].time.Before(p[j].time)
}

func (p actionSlice) Swap(i, j int) {
	p[i], p[j] = p[j], p[i]
}
