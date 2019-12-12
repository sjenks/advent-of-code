class Moon:
	def __init__(self, pos):
		self.pos = pos
		self.vel = [0,0,0]
	def printState(self):
		print("position", self.pos, "velocity", self.vel)

def main():
	numSteps = 5
	moons = []
	moons.append(Moon([-1, 0, 2]))
	moons.append(Moon([2, -10, -7]))
	moons.append(Moon([4, -8, 8]))
	moons.append(Moon([3, 5, -1]))

	for i in range(numSteps):
		print("step", i)
		for m in moons:
			m.printState()
		updateVelocity(moons)
		updatePosition(moons)


def updateVelocity(moons):
	for i in range(len(moons)):
		for j in range(i, len(moons)):
			for axis in range(3):
				updateVelAxis(moons[i], moons[j], axis)

def updateVelAxis(left, right, axis):
	if left.pos[axis] < right.pos[axis]:
		left.vel[axis] += 1
		right.vel[axis] -= 1
	elif left.pos[axis] > right.pos[axis]:
		left.vel[axis] -= 1
		right.vel[axis] += 1
	#else #no velocity change

def updatePosition(moons):
	for moon in moons:
		for axis in range(3):
			moon.pos[axis] += moon.vel[axis] 

if __name__ == "__main__":
	main()