import itertools 

def main():
	ops = parse()
	ampInput = [0, 1, 2, 3, 4]
	maxOutput = -9999999
	for it in itertools.permutations(ampInput):
		ampIn = 0
		for ampSetting in it:
			opsWithInput = []
			[opsWithInput.append(op) for op in ops]
			ampOut = run(opsWithInput, False, ampSetting, ampIn)
			ampIn = ampOut
		if ampOut > maxOutput:
			maxOutput = ampOut
	print("max output found ", maxOutput)

# returns array of ops from the input
def parse():
	filepath = "intcode.txt"

	inputStr = ""
	with open(filepath) as fp:
		for count, line in enumerate(fp):
			inputStr += line

	strOps = inputStr.split(",")
	intOps = []
	[intOps.append(int(op)) for op in strOps]

	return intOps

def run(ops, debugMode, phase, ampSignal):
	programCtr = 0
	iterationCounter = 0
	output = -1

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
			destAddr = ops[programCtr + 1]
			ops[destAddr] = phase
			phase = ampSignal 
			programCtr += 2
		elif ins.opCode == 4: # output
			if ins.isParam1Positional:
				destAddr = ops[programCtr + 1]
				#print(ops[destAddr])
				output = ops[destAddr]
			else:
				#print(ops[programCtr + 1])
				output = ops[programCtr + 1]
			programCtr += 2
		elif ins.opCode == 5: # jmp if true
			left = ops[programCtr + 1]
			if ins.isParam1Positional:
				left = ops[left]
			right = ops[programCtr + 2]
			if ins.isParam2Positional:
				right = ops[right]
			
			if left != 0:
				programCtr = right
			else:
				programCtr += 3
		elif ins.opCode == 6: # jmp if false
			left = ops[programCtr + 1]
			if ins.isParam1Positional:
				left = ops[left]
			right = ops[programCtr + 2]
			if ins.isParam2Positional:
				right = ops[right]
			
			if left == 0:
				programCtr = right
			else:
				programCtr += 3	
		elif ins.opCode == 7: # less than
			left = ops[programCtr + 1]
			if ins.isParam1Positional:
				left = ops[left]
			right = ops[programCtr + 2]
			if ins.isParam2Positional:
				right = ops[right]
			destAddr = ops[programCtr + 3]

			if left < right:
				ops[destAddr] = 1
			else:
				ops[destAddr] = 0
			programCtr += 4
		elif ins.opCode == 8: # less than
			left = ops[programCtr + 1]
			if ins.isParam1Positional:
				left = ops[left]
			right = ops[programCtr + 2]
			if ins.isParam2Positional:
				right = ops[right]
			destAddr = ops[programCtr + 3]

			if left == right:
				ops[destAddr] = 1
			else:
				ops[destAddr] = 0
			programCtr += 4
		else:
			print("invalid opcode " + str(ops[programCtr]) + " at " + str(programCtr))
			return

		iterationCounter += 1
		if debugMode:
			input("iteration " + str(iterationCounter))
			print("opCode: " + str(opCode) + " left: " + str(leftAddr) + " right: " + str(rightAddr) + " dest: " + str(destAddr))
			print(ops)

	return output

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