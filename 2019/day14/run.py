import math

def parse(line):
	output = splitInput(line.split(" => ")[1])
	inputs = line.split(" => ")[0].split(",")
	inputs = [splitInput(ins.strip()) for ins in inputs]
	return (inputs, output)

def splitInput(product):
	spt = product.split(" ")
	return (int(spt[0]), spt[1])

def requirements(lines, item, quantity, extra):
	if item == 'ORE':
		return quantity
	if item in extra:
		quantity -= extra[item]

	extra[item] = 0
	best = -1
	bestAmtSurplus = -1

	for line in lines:
		if line[1][1] == item:
			effectQuant = int(math.ceil(quantity / line[1][0]))
			surplus = effectQuant * line[1][0] - quantity

			if bestAmtSurplus == -1:
				bestAmtSurplus = surplus
			next = 0
			for inp in line[0]:
				req = requirements(lines, inp[1], inp[0] * effectQuant, extra)
				next += req
			if best == -1 or next < best:
				best = next

	extra[item] += bestAmtSurplus

	return best

def guess(lines, incrBy, val):
	while True:
		req = requirements(lines, 'FUEL', val, {})
		if req > 1000000000000: #1 trillion
			return val - incrBy 
		val += incrBy

def main():
	#vscode debugger doesn't like relative paths in windows
	filename = "C:\\Code\\advent-of-code\\2019\\day14\\input.txt" 	
	lines = [parse(line) for line in open(filename).read().split("\n")[:-1]]

	maxProduced = 0
	#guess by powers of 10
	for power in range(10, -1, -1):
		incrBy = 10 ** power
		print("Incr by", incrBy)
		maxProduced = guess(lines, incrBy, maxProduced)

	print(requirements(lines, 'FUEL', 1, {}))

	print(maxProduced)

if __name__ == "__main__":
	main()