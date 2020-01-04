
def main():
	#inputSignal = [1,2,3,4,5,6,7,8]
	numPhases = 100
	filename = "/Users/sjenks/src/advent-of-code/2019/day16/input.txt"
	lines = [list(line) for line in open(filename).read().split("\n")[:-1]]
	inputSignal = [int(i) for i in lines[0]]

	for i in range(numPhases):
		outFft = fftPhase(inputSignal)
		#print(i, outFft)
		inputSignal = outFft

	for i in range(8):
		print(inputSignal[i], end="")
	print()	

def fftPhase(signal):
	nextPhase = [0] * len(signal)

	for outputIdx in range(len(signal)):
		patGen = patternGen(outputIdx)
		next(patGen) #throw away the first pattern

		acc = 0
		for inputSig in signal:
			pattern = next(patGen)
			prod = inputSig * pattern
			acc += prod

		nextPhase[outputIdx] = abs(acc) % 10
		
	return nextPhase

def patternGen(repeat):
	initPattern = [0, 1, 0, -1]
	while True:
		for pat in initPattern:
			for i in range(repeat + 1):
				yield pat

if __name__ == "__main__":
	main()