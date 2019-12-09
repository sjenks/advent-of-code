from enum import Enum

class IntCodeVm:
	OPCODES_WITH_LEFT = []
	def __init__(self, filepath):
		self.filepath = filepath
		self.programCtr = 0
		self.iterationCounter = 0
		self.readPause = False
		self.writePause = False
		self.halted = False
		self.output = -1
		self.input = -1
		self.relativeBase = 0

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

			# all opcodes need at least one param
			left = self.ops[self.programCtr + 1]
			if ins.param1Mode == AddressMode.POSITIONAL:
				left = self.ops[left]
			# but not all need 2 or
			if ins.opCode in [1, 2, 5, 6, 7, 8]:
				right = self.ops[self.programCtr + 2]
				if ins.param2Mode == AddressMode.POSITIONAL:
					right = self.ops[right]

			if ins.opCode == 1: # add
				destAddr = self.ops[self.programCtr + 3] #must be positional
				self.ops[destAddr] = left + right
				self.programCtr += 4
			elif ins.opCode == 2: # mul
				destAddr = self.ops[self.programCtr + 3]
				self.ops[destAddr] = left * right
				self.programCtr += 4
			elif ins.opCode == 3: # input    
				self.readPause = True        
				return
			elif ins.opCode == 4: # output
				self.writePause = True
				if ins.param1Mode == AddressMode.POSITIONAL:
					destAddr = self.ops[self.programCtr + 1]
					#print("output", self.ops[destAddr])
					self.output = self.ops[destAddr]
				else:
					#print("output", self.ops[self.programCtr + 1])
					self.output = self.ops[self.programCtr + 1]
				self.programCtr += 2
				return
			elif ins.opCode == 5: # jmp if true			
				if left != 0:
					self.programCtr = right
				else:
					self.programCtr += 3
			elif ins.opCode == 6: # jmp if false			
				if left == 0:
					self.programCtr = right
				else:
					self.programCtr += 3	
			elif ins.opCode == 7: # less than
				destAddr = self.ops[self.programCtr + 3]

				if left < right:
					self.ops[destAddr] = 1
				else:
					self.ops[destAddr] = 0
				self.programCtr += 4
			elif ins.opCode == 8: # less than
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

		self.halted = True
		return

class Instruction:
	def __init__(self, instruction):
		insStr = str(instruction)
		while(len(insStr) < 5):
			insStr = "0" + insStr

		self.opCode = int(insStr[3:5])
		self.param3Mode = AddressMode(int(insStr[0]))
		self.param2Mode = AddressMode(int(insStr[1]))
		self.param1Mode = AddressMode(int(insStr[2]))

class AddressMode(Enum):
	POSITIONAL = 0
	IMMEDIATE = 1
	OFFSET = 2