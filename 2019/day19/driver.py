from IntCodeVm import IntCodeVm
from enum import Enum
import time

class Driver:
	def readFile(self):
		inputStr = ""
		with open("input.txt") as fp:
			for count, line in enumerate(fp):
				inputStr += line
		self.code = inputStr

	def main(self):
		self.grid = []
		self.readFile()
		for y in range(50):
			row = []
			for x in range(50):
				row.append(0)
			self.grid.append(row)
		
		positionGenerator = self.positionGen

		for position in positionGenerator():
			self.readPosition(position[0], position[1])
		self.printGrid()

	def positionGen(self):
		for y in range(len(self.grid)):
			for x in range(len(self.grid[0])):	
				yield((x,y))

	def readPosition(self, x, y):
		vm = IntCodeVm(None, self.code)
		readX = True
		for i in vm.run():
			if vm.readPause:
				if readX:
					vm.input = x
				else:
					vm.input = y
				readX = not readX
			else:
				self.grid[y][x] = vm.output
		self.grid[y][x] = vm.output

	def printGrid(self):
		paintCnt = 0
		for y in range(len(self.grid)):
			s = ""
			for x in range(len(self.grid[y])):
				if self.grid[y][x] == 0:
					s = s + ' '
				elif self.grid[y][x] == 1:
					s = s + '#'
					paintCnt += 1
				else:
					print("should not get here")
					exit(-1)
			print(s)
		print(paintCnt)

if __name__ == "__main__":
	d = Driver()
	d.main()