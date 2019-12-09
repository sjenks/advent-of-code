import itertools 
from IntCodeVm import IntCodeVm

def main():
	vm = IntCodeVm("C:\\Code\\advent-of-code\\2019\\day09\\input.txt")
	vm.input = 1
	vm.resume()
	while(not vm.halted):
		print(vm.output)
		vm.resume()

if __name__ == "__main__":
	main()