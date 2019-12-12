import math

def main():
	filepath = "input.txt"
	lines = []
	with open(filepath) as fp:
		for count, line in enumerate(fp):
			lines.append(line)
	rawAsteroids = [s.strip() for s in lines]

	asteroids = set()
	for x in range(len(rawAsteroids)):
		for y in range(len(rawAsteroids[x])):
			if rawAsteroids[x][y] == "#":
				astTup = (x,y)
				asteroids.add(astTup)

	stationCnts = []
	for station in asteroids:
		inLOS = lineCount(station, asteroids)
		stationCnts.append((len(inLOS), station, inLOS))
		stationCnts.sort(reverse = True)
		amtInLOS, station, inLOS = stationCnts[0]
	print(amtInLOS)

	destroyed = [(math.atan2(dy, dx), (dx, dy)) for dx, dy in inLOS]
	destroyed.sort(reverse = True)
	dx, dy = destroyed[200 - 1][1]

	x, y = station[0] + dx, station[1] + dy
	while (x, y) not in asteroids:
		x = x + dx
		y = y + dy

	print(y*100 + x)

def lineCount(station, asteroids):
	detected = set()
	for asteroid in asteroids:
		if asteroid != station:
			dx = asteroid[0] - station[0]
			dy = asteroid[1] - station[1]
			g = abs(math.gcd(dx, dy))
			reduced = (dx // g, dy // g)
			detected.add(reduced)
	return detected

if __name__ == "__main__":
	main()