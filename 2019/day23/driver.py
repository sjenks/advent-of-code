from IntCodeVm import IntCodeVm

class Driver:
	def readFile(self):
		inputStr = ""
		with open("/Users/sjenks/src/advent-of-code/2019/day23/input.txt") as fp:
			for count, line in enumerate(fp):
				inputStr += line
		return inputStr

	def main(self):
		code = self.readFile()

		self.vms = []
		self.inited = []
		self.numVms = 50
		self.network = []
		for i in range(self.numVms):
			self.vms.append(IntCodeVm(None, code))
			self.network.append([])
			self.inited.append(False)

		self.emulate()
		
	def emulate(self):
		#init with addresses
		gens = []
		for i in range(self.numVms):
			vm = self.vms[i]
			gens.append(vm.run())

		while True:
			for i in range(self.numVms):
				vm = self.vms[i]
				next(gens[i])
				if vm.readPause:
					if not self.inited[i]:
						vm.input = i
						self.inited[i] = True
					elif len(self.network[i]) > 0:
						packet = self.network[i].pop(0)
						vm.input = packet[0]
						next(gens[i])
						vm.input = packet[1]
					else:
						vm.input = -1
				else: #write pause
					dest = vm.output
					next(gens[i])
					packetX = vm.output
					next(gens[i])
					packetY = vm.output
					if dest == 255:
						print(packetX, packetY)
						exit(1)
					else:
						print("write to ", dest)
						self.network[dest].append((packetX, packetY))


if __name__ == "__main__":
	d = Driver()
	d.main()