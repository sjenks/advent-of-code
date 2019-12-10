

def yld():
	for i in range(4):
		print("start")
		yield 8
		print("end")

for i in yld():
	print(i)

#print("wtf")
#yldTest()
#print("wtf2")
#yldTest()