import itertools 
from IntCodeVm import IntCodeVm

def main():
	ampInput = [0, 1, 2, 3, 4]
	maxOutput = -9999999
	for it in itertools.permutations(ampInput):
		ampIn = 0
		for phase in it:
			vm = IntCodeVm("intcode.txt")
			vm.input = phase
			vm.resume()
			vm.input = ampIn
			vm.resume()
			ampIn = vm.output
		if ampIn > maxOutput:
			maxOutput = ampIn
	print("max output found ", maxOutput)

if __name__ == "__main__":
	main()