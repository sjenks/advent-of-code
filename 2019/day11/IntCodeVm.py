from enum import Enum
from collections import defaultdict
class IntCodeVm:
	def __init__(self, filepath, program = ""):
		self.programCtr = 0
		self.iterationCounter = 0
		self.readPause = False
		self.writePause = False
		self.halted = False
		self.output = -1
		self.input = -1
		self.relativeBase = 0

		self.ops = self.parse(filepath, program)

	# returns array of self.ops from the input
	def parse(self, filepath, program):
		inputStr = ""
		if filepath:
			with open(filepath) as fp:
				for count, line in enumerate(fp):
					inputStr += line
		else:
			inputStr = program

		strOps = inputStr.split(",")
		intOps = defaultdict(int)
		for i in range(len(strOps)):
			converted = int(strOps[i])
			intOps[i] = converted

		return intOps

	def run(self):
		while self.ops[self.programCtr] != 99: # halt
			fullInstruction = self.ops[self.programCtr]
			ins = Instruction(fullInstruction)

			# all opcodes need at least one param
			left = self.ops[self.programCtr + 1]
			if ins.param1Mode == AddressMode.POSITIONAL:
				left = self.ops[left]
			elif ins.param1Mode == AddressMode.RELATIVE:
				left = self.ops[left + self.relativeBase]
			# but not all need 2
			if ins.opCode in [1, 2, 5, 6, 7, 8]:
				right = self.ops[self.programCtr + 2]
				if ins.param2Mode == AddressMode.POSITIONAL:
					right = self.ops[right]
				elif ins.param2Mode == AddressMode.RELATIVE:
					right = self.ops[right + self.relativeBase]
			# or 3.  Note that 3 is still an address
			if ins.opCode in [1, 2, 7, 8]:
				if ins.param3Mode == AddressMode.POSITIONAL:
					destAddr = self.ops[self.programCtr + 3]
				elif ins.param3Mode == AddressMode.RELATIVE:
					destAddr = self.ops[self.programCtr + 3]
					destAddr = destAddr + self.relativeBase
				else: 
					print("should not be here.  cannot write immediate address?")

			# --- START OPCODES --- #
			if ins.opCode == 1: # add
				self.ops[destAddr] = left + right
				self.programCtr += 4
			elif ins.opCode == 2: # mul
				self.ops[destAddr] = left * right
				self.programCtr += 4
			elif ins.opCode == 3: # input 
				self.readPause = True
				yield
				self.readPause = False
				left = self.ops[self.programCtr + 1]
				if ins.param1Mode == AddressMode.POSITIONAL:
					self.ops[left] = self.input
				elif ins.param1Mode == AddressMode.RELATIVE:
					self.ops[left + self.relativeBase] = self.input
				else:
					print("wtf")
				self.programCtr += 2
			elif ins.opCode == 4: # output
				if ins.param1Mode == AddressMode.POSITIONAL:
					destAddr = self.ops[self.programCtr + 1]
					self.output = self.ops[destAddr]
				elif ins.param1Mode == AddressMode.IMMEDIATE:
					self.output = self.ops[self.programCtr + 1]
				elif ins.param1Mode == AddressMode.RELATIVE:
					destAddr = self.ops[self.programCtr + 1] + self.relativeBase
					self.output = self.ops[destAddr]
				self.programCtr += 2
				self.writePause = True
				yield
				self.writePause = False
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
				if left < right:
					self.ops[destAddr] = 1
				else:
					self.ops[destAddr] = 0
				self.programCtr += 4
			elif ins.opCode == 8: # eq to
				if left == right:
					self.ops[destAddr] = 1
				else:
					self.ops[destAddr] = 0
				self.programCtr += 4
			elif ins.opCode == 9: # modify relative base
				self.relativeBase += left
				self.programCtr += 2
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
	RELATIVE = 2