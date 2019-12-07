import itertools 
from IntCodeVm import IntCodeVm

def main():
	ampInput = [5, 6, 7, 8 ,9]
	maxOutput = -9999999
	for it in itertools.permutations(ampInput):
		ampIn = 0
		vms = []
		#initialize vms
		for phase in it:
			vm = IntCodeVm("intcode.txt")
			vm.input = phase
			vm.resume()
			vms.append(vm)

		allHalted = False
		while (not allHalted):
			allHalted = True
			for vm in vms:
				if (not vm.halted):
					vm.input = ampIn
					vm.resume()
					ampIn = vm.output
					allHalted = False

		if ampIn > maxOutput:
			maxOutput = ampIn
	print("max output found ", maxOutput)

def partOne():
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