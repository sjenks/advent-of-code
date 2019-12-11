from IntCodeVm import IntCodeVm
import unittest 

class IntCodeRegression(unittest.TestCase): 
	def test_given2_add(self):
		vm = IntCodeVm(None, "1,0,0,0,4,0")
		next(vm.run())
		self.assertEqual(vm.output, 2, "1+1 should be 2")

	def test_given5_jump1(self):
		vm = IntCodeVm(None, "3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9")
		for i in vm.run():
			vm.input = 5
		self.assertEqual(vm.output, 1, "Should be 1 for non-zero input")
	
	def test_given5_jump2(self):
		vm = IntCodeVm(None, "3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9")
		for i in vm.run():
			vm.input = 0
		self.assertEqual(vm.output, 0, "Should be 0 for zero input")

	def test_given5_range1(self):
		vm = IntCodeVm(None, "3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99")
		for i in vm.run():		
			vm.input = 7
		self.assertEqual(vm.output, 999, "Should be 999 for <8 input")

	def test_given5_range2(self):
		vm = IntCodeVm(None, "3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99")
		for i in vm.run():		
			vm.input = 8
		self.assertEqual(vm.output, 1000, "Should be 1000 for ==8 input")

	def test_given5_range3(self):
		vm = IntCodeVm(None, "3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99")
		for i in vm.run():		
			vm.input = 10
		self.assertEqual(vm.output, 1001, "Should be 1001 for >8 input")

	def test_given9_large_num(self):
		vm = IntCodeVm(None, "104,1125899906842624,99")
		next(vm.run())
		self.assertEqual(vm.output, 1125899906842624, "Should output large num")

	def test_given_large_mul(self):
		vm = IntCodeVm(None, "1102,34915192,34915192,7,4,7,99,0")
		next(vm.run())
		self.assertEqual(vm.output, 1219070632396864, "Should output 16 digit num")
		
	def test_given_offset(self):
		inout = "109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99"
		vm = IntCodeVm(None, inout)
		output = ""
		for i in vm.run():
			output += str(vm.output) + ","
		self.assertEqual(output, inout + ",", "Program should output itself")
if __name__ == '__main__': 
    unittest.main() 