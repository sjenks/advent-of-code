import itertools 
from IntCodeVm import IntCodeVm

def main():
	vm = IntCodeVm("input.txt")
	vm.input = 1
	for i in vm.run():
		print(vm.output)
	
	vm = IntCodeVm("input.txt")
	vm.input = 2
	for i in vm.run():
		print(vm.output)

if __name__ == "__main__":
	main()