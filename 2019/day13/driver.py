from IntCodeVm import IntCodeVm
from enum import Enum
import time

class Driver:
	def main(self):
		self.grid = []
		self.score = []
		for y in range(30):
			row = []
			for x in range(45):
				row.append(0)
			self.grid.append(row)

		self.direction = 0 # 0 degrees
		
		vm = IntCodeVm("input_free.txt")
		vm.input = 0
		paddle = None
		ball = None
		while not vm.halted:
			ins = []
			printcnt = 0
			for i in vm.run():
				if vm.readPause:
					if len(ins) > 0:
						paddle, ball = self.printInstructions(ins)
						ins = []
					vm.input = self.calcInput(paddle, ball)
					#time.sleep(0.02)
				else:
					ins.append(vm.output)
		#vm.dumpState()
		print(self.score)

	def calcInput(self, paddle, ball):
		if paddle == None or ball == None:
			return int(input("direction? "))
		if paddle == (0,0) or ball == (0,0):
			return int(input("direction? "))
		if ball[0] > paddle[0]:
			return 1
		elif ball[0] < paddle[0]:
			return -1
		else:
			return 0

	def printInstructions(self, ins):
			for i in range(0, len(ins), 3):
				x = ins[i]
				y = ins[i+1]
				tile = ins[i+2]
				if x == -1:
					self.score.append(tile)
				else:
					self.grid[y][x] = tile
			return self.printGrid()

	def printGrid(self):
		paintCnt = 0
		paddle = (0,0)
		ball = (0,0)
		for y in range(len(self.grid)):
			s = ""
			for x in range(len(self.grid[y])):
				if self.grid[y][x] == 0:
					s = s + ' '
				elif self.grid[y][x] == 1:
					s = s + chr(9608)
				elif self.grid[y][x] == 2:
					s = s + '.'
				elif self.grid[y][x] == 3:
					paddle = (x,y)
					s = s + '_'
				elif self.grid[y][x] == 4:
					s = s + chr(9679)
					ball = (x,y)
				else:
					print("should not get here")
					exit(-1)
				# if self.grid[y][x] == 2:
				# 	paintCnt += 1
			print(s)
		return paddle, ball
		#print(paintCnt)

if __name__ == "__main__":
	d = Driver()
	d.main()