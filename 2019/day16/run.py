
def partOne():
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

def partTwo():
	numPhases = 100
	filename = "/Users/sjenks/src/advent-of-code/2019/day16/input.txt"
	offset = 5970927 # first 7 digits of input
	lines = [list(line) for line in open(filename).read().split("\n")[:-1]]
	inputSignal = [int(i) for i in lines[0]]
	inputRepeated = inputSignal * 10000

	weights = [1]
	length = len(inputRepeated) - offset
	for i in range(length):
		weights.append(weights[-1] * (100 + i) // (1 + i))

	for idx in range(offset, offset + 8):
		res = outputAt(weights, inputRepeated, idx)
		print(res, end="")
	print()

def outputAt(weights, signal, idx):
	if idx < len(signal) / 2:
		print("offset not in range for estimation")
	backOffset = len(signal) - idx
	fftIters = [weights[i] * signal[i - backOffset] for i in range(backOffset)]
	return sum(fftIters) % 10

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
	#partOne()
	partTwo()