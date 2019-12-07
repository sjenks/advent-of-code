class IntCodeVm:
	def __init__(self, filepath):
		self.filepath = filepath
		self.programCtr = 0
		self.iterationCounter = 0
		self.readPause = False
		self.writePause = False
		self.halted = False
		self.output = -1
		self.input = -1

		self.ops = self.parse()
		self.__run()

	# returns array of self.ops from the input
	def parse(self):
		inputStr = ""
		with open(self.filepath) as fp:
			for count, line in enumerate(fp):
				inputStr += line

		strOps = inputStr.split(",")
		intOps = []
		[intOps.append(int(op)) for op in strOps]

		return intOps

	def resume(self):
		if self.halted:
			print("cannot resume halted program")
			return 

		# input needs to be loaded to memory before resuming
		if self.readPause:
			destAddr = self.ops[self.programCtr + 1]
			self.ops[destAddr] = self.input
			self.programCtr += 2
			self.readPause = False
		# output has already been dumped, and execution can simply resume
		elif self.writePause:
			self.writePause = False
		else:
			print("unexpected resume command")
		self.__run()

	def __run(self):
		if self.readPause or self.writePause or self.halted:
			print("paused!")
			return

		while self.ops[self.programCtr] != 99: # halt
			fullInstruction = self.ops[self.programCtr]
			ins = Instruction(fullInstruction)
			
			if ins.opCode == 1: # add
				left = self.ops[self.programCtr + 1]
				if ins.isParam1Positional:
					left = self.ops[left]
				right = self.ops[self.programCtr + 2]
				if ins.isParam2Positional:
					right = self.ops[right]
				
				destAddr = self.ops[self.programCtr + 3] #must be positional
				self.ops[destAddr] = left + right
				self.programCtr += 4
			elif ins.opCode == 2: # mul
				left = self.ops[self.programCtr + 1]
				if ins.isParam1Positional:
					left = self.ops[left]
				right = self.ops[self.programCtr + 2]
				if ins.isParam2Positional:
					right = self.ops[right]
				destAddr = self.ops[self.programCtr + 3]
				self.ops[destAddr] = left * right
				self.programCtr += 4
			elif ins.opCode == 3: # input    
				self.readPause = True        
				return
			elif ins.opCode == 4: # output
				self.writePause = True
				if ins.isParam1Positional:
					destAddr = self.ops[self.programCtr + 1]
					#print("output", self.ops[destAddr])
					self.output = self.ops[destAddr]
				else:
					#print("output", self.ops[self.programCtr + 1])
					self.output = self.ops[self.programCtr + 1]
				self.programCtr += 2
				return
			elif ins.opCode == 5: # jmp if true
				left = self.ops[self.programCtr + 1]
				if ins.isParam1Positional:
					left = self.ops[left]
				right = self.ops[self.programCtr + 2]
				if ins.isParam2Positional:
					right = self.ops[right]
				
				if left != 0:
					self.programCtr = right
				else:
					self.programCtr += 3
			elif ins.opCode == 6: # jmp if false
				left = self.ops[self.programCtr + 1]
				if ins.isParam1Positional:
					left = self.ops[left]
				right = self.ops[self.programCtr + 2]
				if ins.isParam2Positional:
					right = self.ops[right]
				
				if left == 0:
					self.programCtr = right
				else:
					self.programCtr += 3	
			elif ins.opCode == 7: # less than
				left = self.ops[self.programCtr + 1]
				if ins.isParam1Positional:
					left = self.ops[left]
				right = self.ops[self.programCtr + 2]
				if ins.isParam2Positional:
					right = self.ops[right]
				destAddr = self.ops[self.programCtr + 3]

				if left < right:
					self.ops[destAddr] = 1
				else:
					self.ops[destAddr] = 0
				self.programCtr += 4
			elif ins.opCode == 8: # less than
				left = self.ops[self.programCtr + 1]
				if ins.isParam1Positional:
					left = self.ops[left]
				right = self.ops[self.programCtr + 2]
				if ins.isParam2Positional:
					right = self.ops[right]
				destAddr = self.ops[self.programCtr + 3]

				if left == right:
					self.ops[destAddr] = 1
				else:
					self.ops[destAddr] = 0
				self.programCtr += 4
			else:
				print("invalid opcode " + str(self.ops[self.programCtr]) + " at " + str(self.programCtr))
				return

			self.iterationCounter += 1
			if False: #debug mode
				input("iteration " + str(self.iterationCounter))
				print("opCode: " + str(opCode) + " left: " + str(leftAddr) + " right: " + str(rightAddr) + " dest: " + str(destAddr))
				print(self.ops)
		self.halted = True
		return

class Instruction:
	def __init__(self, instruction):
		insStr = str(instruction)
		while(len(insStr) < 5):
			insStr = "0" + insStr

		self.opCode = int(insStr[3:5])
		self.isParam3Positional = insStr[0] == "0"
		self.isParam2Positional = insStr[1] == "0"
		self.isParam1Positional = insStr[2] == "0"