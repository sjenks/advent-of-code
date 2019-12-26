from IntCodeVm import IntCodeVm

class Driver:
	def main(self):
		vm = IntCodeVm("/Users/sjenks/src/advent-of-code/2019/day25/input.txt")
		outputBuffer = []
		inputBuffer = []
		for _ in vm.run():
			if vm.readPause:
				if len(inputBuffer) == 0:
					buff = input("$ ")
					inputBuffer = [ord(c) for c in buff]
					inputBuffer.append(10) # newline

				c = inputBuffer.pop(0)
				#print(c)
				vm.input = c
			else:
				outRead = vm.output
				if outRead == 10: #newline
					output = ''.join([chr(c) for c in outputBuffer])
					print(output)
					outputBuffer = []
				elif vm.output < 127 and vm.output > 0:
					outputBuffer.append(vm.output)
				else:
					print('hull damage', vm.output)


if __name__ == "__main__":
	d = Driver()
	d.main()