width = 25
height = 6
filepath = "input.txt"

fullText = ""
with open(filepath) as fp:
	for count, line in enumerate(fp):
		fullText = fullText + line

combined = []
for y in range(height):
	ln = []
	for x in range(width):
		ln.append(' ')
	combined.append(ln)

layers = []
layersCount = []
counter = 0
while(counter < len(fullText)):
	curLayer = []
	curCounts = {}
	for y in range(height):
		curLine = []
		for x in range(width):
			char = fullText[counter]
			counter += 1
			curLine.append(char)
			if char in curCounts:
				curCounts[char] = curCounts[char] + 1
			else:
				curCounts[char] = 1
		curLayer.append(curLine)
		layersCount.append(curCounts)
	layers.append(curLayer)

combined = []
for y in range(height):
	ln = []
	for x in range(width):
		ln.append(' ')
	combined.append(ln)

ctr = 0
for i in reversed(range(len(layers))):
	curLayer = layers[i]
	for y in range(height):
		for x in range(width):
			if curLayer[y][x] != "2":
				combined[y][x] = curLayer[y][x]

for y in range(height):
	ln = ""
	for x in range(width):
		if combined[y][x] == "1":
			ln = ln + " "
		else:
			ln = ln + combined[y][x]
	print(ln)
	
minZeros = 9999
minZeroLayer = -1
for i in range(len(layersCount)):
	layerCt = layersCount[i]
	if "0" not in layerCt:
		minZeros = 0
		minZeroLayer = i
	elif layerCt["0"] < minZeros:
		minZeros = layerCt["0"]
		minZeroLayer = i

print(minZeros, minZeroLayer)
print(layersCount[minZeroLayer])
