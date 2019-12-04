def main():
	directions = readDirections()
	firstWire = directionsToLineSegments(directions[0])
	secondWire = directionsToLineSegments(directions[1])

	minDist = 9999999999 #uh, max int?
	for first in firstWire:
		for second in secondWire:
			intersect = findIntersect(first, second)
			if intersect is not None:
				manhattanDist = abs(intersect[0]) + abs(intersect[1])
				print("intersection found", first, second, " at ", intersect, ' dist', manhattanDist)
				minDist = min(minDist, manhattanDist)
	print("min intersection is at " + str(minDist))

def readDirections():
	filepath = "full.txt"

	wires = []
	with open(filepath) as fp:
		for count, line in enumerate(fp):
			wires.append(line.split(","))
	return wires

def directionsToLineSegments(directions):
	last = (0,0) #x,y
	segments = []
	for direction in directions:
		distance = int(direction[1:])
		next = None
		if direction[0] == "R":
			next = (last[0] + distance, last[1])
		elif direction[0] == "L":
			next = (last[0] - distance, last[1])
		elif direction[0] == "U":
			next = (last[0], last[1] + distance)
		elif direction[0] == "D":
			next = (last[0], last[1] - distance)
		else:
			print("error, bad direction" + direction[0])

		seg = (last, next)
		segments.append(seg)
		last = next

	return segments

def findIntersect(left, right):
	#start of left pt
	x1 = left[0][0]
	y1 = left[0][1]
	# end of left pt
	x2 = left[1][0]
	y2 = left[1][1]
	#start of right pt
	x3 = right[0][0]
	y3 = right[0][1]
	#end of right pt
	x4 = right[1][0]
	y4 = right[1][1]

	print(x1, y1, x2, x2, x3, y3, x4, y4)

	leftVert = False
	rightVert = False
	if x1 == x2:
		leftVert = True
	if x3 == x4:
		rightVert = True

	if leftVert and rightVert: # parallel vertical: no intersect
		return None

	if (not leftVert) and (not rightVert): # parallel horizontal: no intersect
		return None

	if rightVert: # swap the two to make our cases simple
		return findIntersect(right, left)
	
	source = (0,0)
	# starts at origin
	if (x3, y1) == source:
		return None

	leftX = x1
	rightY = y3
	if (leftX >= min(x3, x4)) and (leftX <= max(x3, x4)): # left x is between right x's
		if (rightY >= min(y1, y2)) and (rightY <= max(y1, y2)): # right y is between left y's
			return (leftX, rightY)
	return None



if __name__ == "__main__":
	main()