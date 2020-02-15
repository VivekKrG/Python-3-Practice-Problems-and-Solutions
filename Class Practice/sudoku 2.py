import time
import copy


class Sudoku:
	ano_square = {'horizontal': [(1, 2), (-1, 1), (-2, -1)], 'vertical': [(3, 6), (-3, 3), (-6, -3)]}
	move = {'horizontal': [(0, 1, 2), (3, 4, 5), (6, 7, 8)], 'vertical': [(0, 3, 6), (1, 4, 7), (2, 5, 8)]}
	ano_line = [(1, 2), (0, 2), (0, 1)]
	start_time = 0
	wrong_attempts = 0

	def __init__(self):
		# Initialize "blocks" with all possible elements 1-9
		self.blocks = [[{i for i in range(1, 10)} for j in range(9)] for k in range(9)]
		# The "done" matrix will be filled before trying to put all possible elements
		self.done = None  # [[None for i in range(9)] for j in range(9)]
		# The "possible" matrix will be filled with all possible elements at each grid.
		self.possibles = [[set() for i in range(9)] for _ in range(9)]
		# To store solution/s.
		self.solutions = []

	def fill(self, given_sudoku):
		# This method will take inputs for sudoku to be completed and arrange it in block.
		# Here matrix 'blocks' will be filled in a way such that every row will be squares of sudoku moving L->R,
		# starting from top left corner.
		# Every grid of it will be either an element(a set with single element) or set of possible elements.

		self.done = given_sudoku
		input('Click to start time')
		Sudoku.start_time = time.time()

		for i in (0, 3, 6):
			for j in (0, 1, 2):
				for square in (0, 1, 2):
					for grid in (0, 1, 2):
						row = i + square
						col = j * 3 + grid
						square_ = i + j
						grid_ = square * 3 + grid
						if self.done[row][col]:
							self.put_in(square_, grid_, self.done[row][col])

		'''
		for square in range(9):  # Total of 9 squares in Sudoku.
			arr = list(input().split())
			for grid in range(9):
				if arr[grid] is not '.':
					# put_in method will put elements at corresponding grid and eliminate from others to maintain
					# as less 'possible elements' as possible.
					self.put_in(square, grid, int(arr[grid]))
		'''
		print('filling ended: Time elapsed:', time.time() - Sudoku.start_time)
		print('Going to complete')

		# complete is a method from where some simple algorithms will be used and elements will be filled accordingly.
		self.complete()

	def put_in(self, square, grid, element):
		# Firstly, eliminate same number from all other grid of the same square.
		for self_grid in range(9):
			# if len(self.blocks[square][self_grid]) > 1:
			self.blocks[square][self_grid].discard(element)
			if grid != self_grid and len(self.blocks[square][self_grid]) == 0:
				return False

			# After eliminating, if only one element is possible at a location,
			# then again put it at the same location. This will minimise possible elements recursively.
			if len(self.blocks[square][self_grid]) == 1:
				self.put_in(square, self_grid, self.blocks[square][self_grid].pop())

		# Now put given element at given location.
		self.blocks[square][grid] = {element}

		# Now, eliminate numbers from same row and column of other squares.
		row, col = divmod(square, 3)
		grid_row, grid_col = divmod(grid, 3)

		for direction in ('horizontal', 'vertical'):
			select_square = col if direction is 'horizontal' else row
			for i in Sudoku.ano_square[direction][select_square]:
				select_line = grid_row if direction is 'horizontal' else grid_col
				for j in Sudoku.move[direction][select_line]:
					# if len(self.blocks[square+i][j]) > 1:
					self.blocks[square+i][j].discard(element)
					reduced_len = len(self.blocks[square + i][j])
					if reduced_len == 0:
						return False
					elif reduced_len == 1:
						self.put_in(square+i, j, self.blocks[square + i][j].pop())
		return True

	def complete(self):
		for _ in range(2):
			for square in range(9):
				for grid in range(9):
					if len(self.blocks[square][grid]) > 1:
						# If a element have only one possible location, then put that element at there.
						self.eliminate_in_square(square, grid)

			for square in range(9):
				for line in (0, 1, 2):
					# For a row/column of a square, if a element is present at other 2 rows/columns of other 2 square,
					# then that element must be in that row/column of a square.
					# In that row/column, if a element have a single possible grid, then put it there.
					self.select_right_elements(square, line, 'horizontal')
					self.select_right_elements(square, line, 'vertical')

		print('Completing done: Time elapsed: ', time.time() - Sudoku.start_time)
		# Up-to now, matrix 'blocks' is filled using general algorithms.

		# Now, Backtracking will be used to complete rest of the grids with the help of matrix 'possible'.
		# It is found that, backtracking takes too much time to give first solution if it is used on matrix 'blocks'.
		# So, matrix 'done' is to be filled in a manner as sudoku is filled. At the same time,
		# matrix 'possible' will be filled with set of possible elements.
		self.fill_done()
		# for rows in range(9):
		# 	print(self.done[rows])
		# print('8888888*************8888')
		# for rows in range(9):
		# 	print(self.possibles[rows])

		# Use backtracking.
		self.try_all()

	def select_right_elements(self, square, line, direction):
		row, col = divmod(square, 3)
		select_square = col if direction is 'horizontal' else row
		first = set()
		for i in Sudoku.ano_square[direction][select_square]:
			for j in Sudoku.move[direction][Sudoku.ano_line[line][0]]:
				first |= self.blocks[square+i][j]

		second = set()
		for i in Sudoku.ano_square[direction][select_square]:
			for j in Sudoku.move[direction][Sudoku.ano_line[line][1]]:
				second |= self.blocks[square+i][j]

		right_elements = first & second
		for j in Sudoku.move[direction][line]:
			if self.done[square][j] is None:
				possibles = self.blocks[square][j] & right_elements
				if len(possibles) is 1:
					self.put_in(square, j, possibles.pop())
				elif len(possibles) < len(self.blocks[square][j]):
					self.blocks[square][j] = possibles

	def eliminate_in_square(self, square, grid):
		union = set()
		for self_grid in range(9):
			if len(self.blocks[square][self_grid]) > 1 and self_grid != grid:
				union |= self.blocks[square][self_grid]
		diff = self.blocks[square][grid] - union
		if len(diff) == 1:
			self.put_in(square, grid, diff.pop())

	def fill_done(self):
		for i in (0, 3, 6):
			for j in (0, 1, 2):
				for square in (0, 1, 2):
					for grid in (0, 1, 2):
						row = i + square
						col = j * 3 + grid
						row_ = i + j
						col_ = square*3 + grid
						if len(self.blocks[row][col]) == 1:
							self.done[row_][col_] = self.blocks[row][col].pop()
						else:
							self.possibles[row_][col_] = self.blocks[row][col]

	def safe_to_put(self, square, grid, element):
		# Check whether it used in row
		for col in range(9):
			if self.done[square][col] == element:
				return False

		# Check whether it used in column
		for row in range(9):
			if self.done[row][grid] == element:
				return False

		# Check whether it used in square
		row = square - square % 3
		col = grid - grid % 3
		for i in range(3):
			for j in range(3):
				if self.done[row+i][col+j] == element:
					return False

		# If all above if not true, then element can be used.
		# So return True
		return True

	def put_in_try(self, square, grid, element):
		if self.safe_to_put(square, grid, element):
			self.done[square][grid] = element
			return True
		else:
			return False

	def get_vacant_place(self):
		for square in range(9):
			for grid in range(9):
				if not self.done[square][grid]:
					return square, grid
		return False

	def try_all(self):
		vacant = self.get_vacant_place()
		if vacant:
			square = vacant[0]
			grid = vacant[1]
			for element in self.possibles[square][grid]:
				if self.put_in_try(square, grid, element):  # It returns True after putting
					if self.try_all():
						return True
					Sudoku.wrong_attempts += 1
					self.done[square][grid] = None
		else:  # There is no vacant place to fill, hence we've done!!!
			self.solutions.append(copy.deepcopy(self.done[:]))
			# Return False multiple time to get multiple solution if exist.
			return True #if len(self.solutions) > 9 else False
		return False


if __name__ == '__main__':
	input_sudoku = [[0, 9, 4, 0, 5, 0, 2, 0, 7],
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

	sudoku = Sudoku()
	sudoku.fill(grid3)
	print()

	print("--- %s seconds ---" % (time.time() - Sudoku.start_time))
	print('Number of wrong attempts: ', Sudoku.wrong_attempts)
	# for k in range(9):
	# 	print(sudoku.blocks[k])
	# print('---------------------------------------------------------------------------')
	# print(sudoku.solutions)
	for sol in sudoku.solutions:
		print('from solutions---------------------------------------')
		for sq in sol:
			print(sq)

'''
. 9 4 7 . . . . 2
. 5 . . . 9 1 . 4
2 . 7 . . 1 . 8 .
2 . . . . 3 . 6 . 
9 . . . . 6 . 1 .
6 . 8 . 9 . . . 4
4 1 . . . 8 9 . .
8 3 . . 9 . 4 . 1
9 . . . 1 . . . 3

Number of wrong attempts:  4
[{1}, {9}, {4}, {7}, {8}, {5}, {6}, {3}, {2}]
[{3}, {5}, {8}, {2, 6}, {2, 6}, {9}, {1}, {7}, {4}]
[{2}, {6}, {7}, {3}, {4}, {1}, {5}, {8}, {9}]
[{2}, {7}, {1}, {5}, {4}, {3}, {8}, {6}, {9}]
[{9}, {4}, {3, 5}, {7}, {8}, {6}, {2, 5}, {1}, {2, 3, 5}]
[{6}, {3, 5}, {8}, {1}, {9}, {2}, {7}, {3, 5}, {4}]
[{4}, {1}, {6, 7}, {3}, {2}, {8}, {9}, {5}, {6, 7}]
[{8}, {3}, {2, 5}, {5, 6}, {9}, {7}, {4}, {2, 6}, {1}]
[{9}, {2, 7}, {5, 6}, {4}, {1}, {5, 6}, {8}, {2, 7}, {3}]

'''
