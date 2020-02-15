import time


def print_grid(arr):
	for i in range(9):
		for j in range(9):
			print(arr[i][j], end=' ')
		print('n')


def find_empty_location(arr):
	global l
	sq_start = 1  # l[0]  # l[0]
	g_start = 1  # l[1] + 1
	for row in range(sq_start, 10):
		for col in range(g_start, 10):
			if arr[-row][-col] == 0:
				l[0] = -row
				l[1] = -col
				return True
	return False


def used_in_row(arr, row, num):
	for i in range(9):
		if arr[row][i] == num:
			return True
	return False


def used_in_col(arr, col, num):
	for i in range(9):
		if arr[i][col] == num:
			return True
	return False


def used_in_box(arr, row, col, num):
	for i in range(3):
		for j in range(3):
			# print(i+row, j+col)
			if arr[i + row][j + col] == num:
				return True
	return False


def check_location_is_safe(arr, row, col, num):
	return not used_in_row(arr, row, num) and\
			not used_in_col(arr, col, num) and\
			not used_in_box(arr, row - row % 3, col - col % 3, num)


def solve_sudoku(arr):
	global count
	global l

	if not find_empty_location(arr):
		return True

	row = l[0]
	col = l[1]

	for num in range(1, 10):
		if check_location_is_safe(arr, row, col, num):
			arr[row][col] = num
			if solve_sudoku(arr):
				return True
			count += 1
			arr[row][col] = 0

			# l[0] -= 1
			# if l[0] == -1:
			# 	l[0] = 0
			# l[1] = 0

	return False


l = [0, 0]
count = 0


if __name__ == "__main__":

	grid = [[0 for x in range(9)] for y in range(9)]

	grid = [[0, 9, 4, 0, 5, 0, 2, 0, 7],
			[7, 0, 0, 0, 0, 9, 0, 0, 1],
			[0, 0, 2, 1, 0, 4, 0, 8, 0],
			[2, 0, 0, 9, 0, 0, 6, 0, 8],
			[0, 0, 3, 0, 0, 6, 0, 9, 0],
			[0, 6, 0, 0, 1, 0, 0, 0, 4],
			[4, 1, 0, 8, 3, 0, 9, 0, 0],
			[0, 0, 8, 0, 9, 0, 0, 1, 0],
			[9, 0, 0, 4, 0, 1, 0, 0, 3]]

	grid2 = [[0, 9, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 3, 0, 0, 6, 0, 9, 0],
			[0, 6, 0, 0, 1, 0, 0, 0, 4],
			[4, 1, 0, 8, 3, 0, 9, 0, 0],
			[0, 0, 8, 0, 9, 0, 0, 1, 0],
			[0, 0, 0, 4, 0, 0, 0, 0, 3]]

	grid3 = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
	        [6, 0, 0, 1, 9, 5, 0, 0, 0],
	        [0, 9, 8, 0, 0, 0, 0, 6, 0],
	        [8, 0, 0, 0, 6, 0, 0, 0, 3],
	        [4, 0, 0, 8, 0, 3, 0, 0, 1],
	        [7, 0, 0, 0, 2, 0, 0, 0, 6],
	        [0, 6, 0, 0, 0, 0, 4, 8, 0],
	        [0, 0, 0, 4, 1, 9, 0, 0, 5],
	        [0, 0, 0, 0, 8, 0, 0, 7, 9]]

	grid4 = [[0, 9, 0, 0, 0, 0, 0, 0, 0],
	         [0, 0, 0, 0, 0, 0, 0, 0, 0],
	         [0, 0, 0, 0, 0, 0, 0, 0, 0],
	         [0, 0, 0, 0, 0, 0, 0, 0, 0],
	         [0, 0, 3, 0, 0, 6, 0, 9, 0],
	         [0, 6, 0, 0, 1, 0, 0, 0, 4],
	         [4, 1, 0, 8, 3, 0, 9, 0, 0],
	         [0, 0, 8, 0, 9, 0, 4, 1, 0],
	         [0, 0, 0, 4, 0, 1, 0, 0, 3]]

	# Wrong input
	grid5 = [[5, 3, 2, 6, 7, 8, 9, 1, 4],
			[6, 0, 5, 1, 9, 5, 3, 2, 8],
			[1, 9, 8, 3, 4, 2, 5, 6, 7],
			[8, 1, 9, 7, 6, 4, 2, 5, 3],
			[4, 2, 6, 8, 5, 3, 7, 9, 1],
			[7, 5, 3, 9, 2, 1, 8, 4, 6],
			[9, 6, 1, 5, 3, 7, 4, 8, 2],
			[2, 8, 7, 4, 1, 9, 6, 3, 5],
			[3, 5, 4, 2, 8, 6, 1, 7, 9]]

	start_time = time.time()
	if solve_sudoku(grid5):
		print_grid(grid5)
	else:
		print("No solution exists")
	print("--- %s seconds ---" % (time.time() - start_time))
	print(count)

'''
1 9 2 3 4 5 6 7 8 n
3 5 4 6 7 8 1 2 9 n
7 8 6 1 2 9 3 4 5 n
2 7 1 9 5 4 8 3 6 n
5 4 3 2 8 6 7 9 1 n
8 6 9 7 1 3 2 5 4 n
4 1 5 8 3 2 9 6 7 n
6 3 8 5 9 7 4 1 2 n
9 2 7 4 6 1 5 8 3 n
--- 22.078731060028076 seconds ---
537420
Running from dense side
--- 0.00802159309387207 seconds ---
108

1 9 4 3 5 8 2 6 7 n
7 8 5 2 6 9 3 4 1 n
6 3 2 1 7 4 5 8 9 n
2 7 1 9 4 3 6 5 8 n
5 4 3 7 8 6 1 9 2 n
8 6 9 5 1 2 7 3 4 n
4 1 7 8 3 5 9 2 6 n
3 2 8 6 9 7 4 1 5 n
9 5 6 4 2 1 8 7 3 n
--- 0.005013465881347656 seconds ---
66

'''