import itertools 
from IntCodeVm import IntCodeVm
class Driver:
	def main(self):
		self.grid = []
		for y in range(100):
			row = []
			for x in range(100):
				row.append('.')
			self.grid.append(row)

		self.curX = 50
		self.curY = 50
		self.grid[50][50] = "W" #part 2
		self.direction = 0 # 0 degrees
		
		vm = IntCodeVm("input.txt")
		vm.input = 0
		paint = []
		for i in vm.run():
			if vm.readPause:
				if self.grid[self.curY][self.curX] == "W": # white
					vm.input = 1
				else:
					vm.input = 0
			else:
				if len(paint) < 1:
					paint.append(vm.output)
				else:
					directionOut = vm.output
					self.updatePosition(paint[0], directionOut)
					self.curX, self.curY = self.nextPosition(self.curX, self.curY, self.direction)
					paint = []
		self.printGrid()

	def updatePosition(self, paint, directionOut):
		if paint == 1:
			self.grid[self.curY][self.curX] = 'W'
		else:
			self.grid[self.curY][self.curX] = 'B'
		if directionOut == 0:
			self.direction -= 90
			if self.direction == -90:
				self.direction = 270
		else:
			self.direction += 90
			if self.direction == 360:
				self.direction = 0

	def nextPosition(self, x, y, direction):
		if direction == 0:
			return x, (y - 1)
		elif direction == 90:
			return (x + 1), y
		elif direction == 180:
			return x, (y + 1)
		elif direction == 270:
			return (x - 1), y
		else:
			print("error - not grid alligned", direction)
	def printGrid(self):
		paintCnt = 0
		for y in range(len(self.grid)):
			s = ""
			for x in range(len(self.grid)):
				if self.grid[y][x] != '.':
					paintCnt += 1
				if self.grid[y][x] == "W":
					s = s + self.grid[y][x]
				else:
					s = s + "."
			print(s)
		
		print(paintCnt)

if __name__ == "__main__":
	d = Driver()
	d.main()