from IntCodeVm import IntCodeVm
from enum import Enum
import time
import queue

class Driver:
	def readFile(self):
		inputStr = ""
		with open("input.txt") as fp:
			for count, line in enumerate(fp):
				inputStr += line
		self.code = inputStr

	def main(self):
		self.grid = {}
		self.readFile()		
		bottomGenerator = self.probeBottom()

		while True:
			position = next(bottomGenerator)
			self.readPosition(position[0], position[1])

	def probeBottom(self):
		next = (11, 10)

		#go down one, and right until back in the #'s
		while(True):
			next = (next[0], next[1] + 1)
			if(next not in self.grid):
				yield next
			
			while next not in self.grid or self.grid[next] == 0:
				if next not in self.grid:
					yield next
				elif self.grid[next] == 0:
					next = (next[0] + 1, next[1])
			
			##### check the spot
			for i in range(150):
				pos = (next[0] + i, next[1])
				squareGen = self.checkIf100Sq(pos)
				for i in squareGen:
					yield i


	def checkIf100Sq(self, position):
		current = position
		lineSize = 100
		found = False
		while not found:
			#fill in lines
			for x in range(lineSize):
				next = (current[0] + x, current[1])
				if next not in self.grid:
					yield next
				if self.grid[next] == 0:
					return False
			for y in range(lineSize):
				next = (current[0], current[1] + y)
				if next not in self.grid:
					yield next
				if self.grid[next] == 0:
					return False
			
			print("found it? ", current)
			exit(1)

	def readPosition(self, x, y):
		print('reading', x, y)
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
				self.grid[(x,y)] = vm.output
		self.grid[(x,y)] = vm.output

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