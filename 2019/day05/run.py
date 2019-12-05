def main():
	ops = parse()
	opsWithInput = []
	[opsWithInput.append(op) for op in ops]

	output = run(opsWithInput, False)

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
		fullInstruction = ops[programCtr]
		ins = Instruction(fullInstruction)
		
		if ins.opCode == 1: # add
			left = ops[programCtr + 1]
			if ins.isParam1Positional:
				left = ops[left]
			right = ops[programCtr + 2]
			if ins.isParam2Positional:
				right = ops[right]
			
			destAddr = ops[programCtr + 3] #must be positional
			ops[destAddr] = left + right
			programCtr += 4
		elif ins.opCode == 2: # mul
			left = ops[programCtr + 1]
			if ins.isParam1Positional:
				left = ops[left]
			right = ops[programCtr + 2]
			if ins.isParam2Positional:
				right = ops[right]
			destAddr = ops[programCtr + 3]
			ops[destAddr] = left * right
			programCtr += 4
		elif ins.opCode == 3: # input
			consoleIn = int(input("input requested"))
			destAddr = ops[programCtr + 1]
			ops[destAddr] = consoleIn
			programCtr += 2
		elif ins.opCode == 4: # output
			if ins.isParam1Positional:
				destAddr = ops[programCtr + 1]
				print(ops[destAddr])
			else:
				print(ops[programCtr + 1])
			programCtr += 2
		else:
			print("invalid opcode " + str(ops[programCtr]) + " at " + str(programCtr))
			return

		iterationCounter += 1
		if debugMode:
			input("iteration " + str(iterationCounter))
			print("opCode: " + str(opCode) + " left: " + str(leftAddr) + " right: " + str(rightAddr) + " dest: " + str(destAddr))
			print(ops)
	print("halted, output at zero is" + str(ops[0]))
	return ops[0]

class Instruction:
	def __init__(self, instruction):
		insStr = str(instruction)
		while(len(insStr) < 5):
			insStr = "0" + insStr

		self.opCode = int(insStr[3:5])
		self.isParam3Positional = insStr[0] == "0"
		self.isParam2Positional = insStr[1] == "0"
		self.isParam1Positional = insStr[2] == "0"

if __name__ == "__main__":
	main()