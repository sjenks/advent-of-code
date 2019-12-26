
filepath = "/Users/sjenks/src/advent-of-code/2019/day25/input.txt"

inputStr = ""
with open(filepath) as fp:
	for count, line in enumerate(fp):
		inputStr += line

ins = inputStr.split(',')

for strins in ins:
	i = int(strins)
	if i < 128 and i > 47:
		print(chr(i - 13), end = "")
print("")