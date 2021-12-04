def main():
	filepath = "input.txt"

	with open(filepath) as f:
		lines = f.readlines()
	num_draw = lines[0].split(',')
	numbers_drawn = [int(c) for c in num_draw]

	num_boards = (len(lines) - 1) // 6
	print('boards' + str(num_boards))

	boards = []
	for i in range(num_boards):
		start_ln = (i*6)+1
		board = read_board(lines, start_ln)
		#print(board)
		boards.append(board)

	remaining = [i for i in range(len(boards))]
	print(remaining)
	for drawn in numbers_drawn:
		for board_idx in range(len(boards)):
			board = boards[board_idx]
			if board_idx not in remaining:
				continue
			else:
				mark_board(board, drawn)
				has_won = check_for_win(board)
				if has_won and len(remaining) == 1:
					print('winner found')
					print(f'number drawn{drawn}' )
					board_sum = unmarked_board_sum(board)
					print(f'board sum{board_sum}')
					score = board_sum * drawn
					print(f'score {score}')
					print(board)
					return
				elif has_won:
					print(f'removing board num{board_idx}')
					remaining.remove(board_idx)


def unmarked_board_sum(board):
	board_sum = 0
	for row in board:
		for val in row:
			if val[1] == False:
				board_sum += val[0]
	return board_sum

def read_board(lines, start_ln):
	board = []
	for i in range(start_ln + 1, start_ln + 6):
		cur_line = lines[i].strip().split(' ')
		ints = []
		for c in cur_line:
			if c != '':
				num = int(c)
				ints.append((num, False))
		board.append(ints)
	return board

def check_for_win(board):
	#check rows
	for row in board:
		all_true = True
		for val in row:
			if val[1] == False:
				all_true = False
		if all_true:
			return True
	
	#check cols
	for col_idx in range(5):
		all_true = True
		for row_idx in range(5):
			val = board[row_idx][col_idx]
			if val[1] == False:
				all_true = False
		if all_true:
			return True

	return False

def mark_board(board, check_for_num):
	for i in range(len(board)):
		for j in range(len(board[i])):
			if board[i][j][0] == check_for_num:
				board[i][j] = (check_for_num, True)

if __name__ == "__main__":
	main()


		#for board in boards:
		#	mark_board(board, drawn)
		#	has_won = check_for_win(board)
			# if has_won:
			# 	print('winner found')
			# 	print(f'number {drawn}' )
			# 	board_sum = unmarked_board_sum(board)
			# 	print(f'board sum{board_sum}')
			# 	score = board_sum * drawn
			# 	print(f'score {score}')
			# 	#print(board)