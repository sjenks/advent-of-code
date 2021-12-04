
def main():
	foo = 1
	pub1 = 10441485
	pub2 = 1004920
	#pub1 = 5764801
	#pub2 = 17807724

	loop_size_1 = get_loop_new(pub1)
	print(f'got transform 1  {loop_size_1}')
	loop_size_2 = get_loop_new(pub2)
	print(f'got transform 2  {loop_size_2}')

	res = transform(pub2, loop_size_1)
	print(res)
	res = transform(pub1, loop_size_2)
	print(res)

def get_loop_new(pub):
	loop_size = 1
	while True:
		if pow(7, loop_size, 20201227) == pub:
			return loop_size
		loop_size += 1

if __name__ == "__main__":
	main()