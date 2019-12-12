import math
class Moon:
	def __init__(self, pos):
		self.pos = pos
		self.vel = [0,0,0]
	def stringify(self):
		return str(self.pos) + str(self.vel)
	def printState(self):
		print("position", self.pos, "velocity", self.vel)

def main():
	numSteps = 1000
	moons = []
	# given example
	# moons.append(Moon([-1, 0, 2]))
	# moons.append(Moon([2, -10, -7]))
	# moons.append(Moon([4, -8, 8]))
	# moons.append(Moon([3, 5, -1]))

	# input
	moons.append(Moon([-15, 1, 4]))
	moons.append(Moon([1, -10, -8]))
	moons.append(Moon([-5, 4, 9]))
	moons.append(Moon([4, 6, -2]))

	#for i in range(numSteps + 1):
	intervals = {}
	for axis in range(3):
		seen = set()
		step = 0
		while True:
			# print("step", i)
			# for m in moons:
			# 	m.printState()
			# print("totalEnergy", totalEnergy(moons))
			key = ""
			for m in moons:
				key += str(m.pos[axis])
				key += str(m.vel[axis])
			if key in seen:
				intervals[axis] = step
				break
			else:
				seen.add(key)
			updateVelocity(moons, axis)
			updatePosition(moons, axis)
			step += 1
	print(lcm(intervals[0], lcm(intervals[1], intervals[2])))

def updateVelocity(moons, axis):
	for i in range(len(moons)):
		for j in range(i, len(moons)):
			updateVelAxis(moons[i], moons[j], axis)

def updateVelAxis(left, right, axis):
	if left.pos[axis] < right.pos[axis]:
		left.vel[axis] += 1
		right.vel[axis] -= 1
	elif left.pos[axis] > right.pos[axis]:
		left.vel[axis] -= 1
		right.vel[axis] += 1

def updatePosition(moons, axis):
	for moon in moons:
		moon.pos[axis] += moon.vel[axis] 

def totalEnergy(moons):
	total = 0
	for moon in moons:
		moonPot = 0
		moonKin = 0
		for axis in range(3):
			moonPot += abs(moon.pos[axis])
			moonKin += abs(moon.vel[axis])
		total += (moonPot * moonKin)
	return total

def lcm(x, y):
   lcm = (x*y)//math.gcd(x,y)
   return lcm

if __name__ == "__main__":
	main()