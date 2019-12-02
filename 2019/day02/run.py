def main():
	ops = parse()

	for noun in range(99):
		for verb in range(99):
			opsWithInput = []
			[opsWithInput.append(op) for op in ops]
			opsWithInput[1] = noun
			opsWithInput[2] = verb
			output = run(opsWithInput, False)
			if output == 19690720:
				print("noun" + str(noun) + " verb " + str(verb))
				return

# returns array of ops from the input
def parse():
	filepath = "input.txt"

	inputStr = ""
	with open(filepath) as fp:
		for count, line in enumerate(fp):
			inputStr += line

	strOps = inputStr.split(",")
	intOps = []
	[intOps.append(int(op)) for op in strOps]

	return intOps

def run(ops, debugMode):
	programCtr = 0
	iterationCounter = 0

	while ops[programCtr] != 99: # halt
		opCode = ops[programCtr]
		leftAddr = ops[programCtr + 1]
		rightAddr = ops[programCtr + 2]
		destAddr = ops[programCtr + 3]
		if opCode == 1: # add

			ops[destAddr] = ops[leftAddr] + ops[rightAddr]
		elif opCode == 2: # mul
			ops[destAddr] = ops[leftAddr] * ops[rightAddr]
		else:
			print("invalid opcode " + str(ops[programCtr]) + " at " + str(programCtr))

		programCtr += 4
		iterationCounter += 1
		if debugMode:
			input("iteration " + str(iterationCounter))
			print("opCode: " + str(opCode) + " left: " + str(leftAddr) + " right: " + str(rightAddr) + " dest: " + str(destAddr))
			print(ops)
	print("halted, output at zero is" + str(ops[0]))
	return ops[0]


if __name__ == "__main__":
	main()