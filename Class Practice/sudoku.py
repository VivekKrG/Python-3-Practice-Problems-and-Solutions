import copy
import time


class Square:
	def __init__(self):
		self.square = [{i for i in range(1, 10)} for j in range(9)]

	def __str__(self):
		return str(self.square)


class Sudoku:
	ano_square = {'horizontal': [(1, 2), (-1, 1), (-2, -1)], 'vertical': [(3, 6), (-3, 3), (-6, -3)]}
	move = {'horizontal': [(0, 1, 2), (3, 4, 5), (6, 7, 8)], 'vertical': [(0, 3, 6), (1, 4, 7), (2, 5, 8)]}
	ano_line = [(1, 2), (0, 2), (0, 1)]
	start_time = 0
	wrong_attempts = 0

	def __init__(self):
		self.blocks = [Square() for i in range(9)]
		self.done = [[None for i in range(9)] for j in range(9)]
		self.solutions = []

	def __str__(self):
		return str(self.blocks)

	def fill(self):
		# This method will take inputs for sudoku to be completed and arrange it in block.

		input('Click to start time')
		Sudoku.start_time = time.time()

		for square in range(9):
			arr = list(input().split())
			for grid in range(9):
				if arr[grid] is not '.':
					self.put_in(square, grid, int(arr[grid]))

		print('filling ended: Time elapsed:', time.time() - Sudoku.start_time)
		print('Going to complete')
		# Complete is a method from where all possibilities will be checked and elements will be filled accordingly.
		self.complete()

	def put_in(self, square, grid, element):
		for self_grid in range(9):
			self.blocks[square].square[self_grid].discard(element)
		self.blocks[square].square[grid] = {element}
		self.done[square][grid] = element

		for self_grid in range(9):
			if len(self.blocks[square].square[self_grid]) == 1 and not self.done[square][self_grid]:
				self.put_in(square, self_grid, self.blocks[square].square[self_grid].pop())

		row, col = divmod(square, 3)
		grid_row, grid_col = divmod(grid, 3)

		for direction in ('horizontal', 'vertical'):
			select_square = col if direction is 'horizontal' else row
			for i in Sudoku.ano_square[direction][select_square]:
				select_line = grid_row if direction is 'horizontal' else grid_col
				for j in Sudoku.move[direction][select_line]:
					self.blocks[square+i].square[j].discard(element)
					if len(self.blocks[square+i].square[j]) == 1 and not self.done[square+i][j]:
						self.put_in(square+i, j, list(self.blocks[square+i].square[j])[0])

	def select_right_elements(self, square, line, direction):
		row, col = divmod(square, 3)
		select_square = col if direction is 'horizontal' else row
		first = set()
		for i in Sudoku.ano_square[direction][select_square]:
			for j in Sudoku.move[direction][Sudoku.ano_line[line][0]]:
				first |= self.blocks[square+i].square[j]

		second = set()
		for i in Sudoku.ano_square[direction][select_square]:
			for j in Sudoku.move[direction][Sudoku.ano_line[line][1]]:
				second |= self.blocks[square+i].square[j]

		right_elements = first & second
		for j in Sudoku.move[direction][line]:
			if not self.done[square][j]:
				possibles = self.blocks[square].square[j] & right_elements
				if len(possibles) is 1:
					self.put_in(square, j, possibles.pop())
				elif len(possibles) < len(self.blocks[square].square[j]):
					self.blocks[square].square[j] = possibles

	def eliminate_in_square(self, square, grid):
		union = set()
		for self_grid in range(9):
			if len(self.blocks[square].square[self_grid]) > 1 and self_grid != grid:
				union |= self.blocks[square].square[self_grid]
		diff = self.blocks[square].square[grid] - union
		if len(diff) == 1:
			self.put_in(square, grid, diff.pop())

	def complete(self):
		for _ in range(2):
			for square in range(9):
				for grid in range(9):
					if len(self.blocks[square].square[grid]) > 1:
						self.eliminate_in_square(square, grid)
			for square in range(9):
				for line in (0, 1, 2):
					self.select_right_elements(square, line, 'horizontal')

				for vertical in (0, 1, 2):
					self.select_right_elements(square, vertical, 'vertical')
		print('Completing done: Time elapsed: ', time.time() - Sudoku.start_time)
		for rows in range(9):
			print(self.done[rows])
		self.try_all()

	def safe_to_put(self, square, grid, element):
		row, col = divmod(square, 3)
		grid_row, grid_col = divmod(grid, 3)

		for direction in ('horizontal', 'vertical'):
			select_square = col if direction is 'horizontal' else row
			for i in Sudoku.ano_square[direction][select_square]:
				select_line = grid_row if direction is 'horizontal' else grid_col
				for j in Sudoku.move[direction][select_line]:
					if element == self.done[square+i][j]:
						return False
		# Check for self square
		for self_element in self.done[square]:
			if self_element == element:
				return False
		return True

	def put_in_try(self, square, grid, element):
		if self.safe_to_put(square, grid, element):
			self.done[square][grid] = element
			return True
		else:
			return False

	def get_vacant_place(self):
		# for square in range(9):
		# 	for grid in range(9):
		# 		if not self.done[square][grid]:
		# 			return square, grid
		# return False
		for i in (0, 1, 2):
			for j in (0, 1, 2):
				for square in (0, 1, 2):
					for grid in (0, 1, 2):
						if not self.done[i*3+square][j*3+grid]:
							return i*3+square, j*3+grid
		return False

	def try_all(self):
		vacant = self.get_vacant_place()
		if vacant:
			square = vacant[0]
			grid = vacant[1]
			for element in self.blocks[square].square[grid]:
				if self.put_in_try(square, grid, element):  # Return True after putting
					if self.try_all():
						return True
					Sudoku.wrong_attempts += 1
					self.done[square][grid] = None
		else:  # There is no vacant place to fill, hence we've done!!!
			self.solutions.append(copy.deepcopy(self.done))
			# for rows in range(9):
			# 	print(self.done[rows])
			# print('----------------------------------------------------------------------------')
			# Return True to explore all possible solutions, otherwise return True.
			return True #if len(self.solutions) > 9 else False
		return False


sqr = Square()
print(sqr)
sudoku = Sudoku()
sudoku.fill()
print()

print("--- %s seconds ---" % (time.time() - Sudoku.start_time))
print('Number of wrong attempts: ', Sudoku.wrong_attempts)
for k in range(9):
	print(sudoku.blocks[k])
# print('---------------------------------------------------------------------------')
# print(sudoku.solutions)
for sol in sudoku.solutions:
	print('from solutions---------------------------------------')
	for sq in sol:
		print(sq)


'''
. 9 4 7 2 . . . 2
. 5 . . . 9 1 . 4
2 . 7 . . 1 . 8 .
2 . . . . 3 . 6 . 
9 . . . . 6 . 1 .
6 . 8 . 9 . . . 4
4 1 . . . 8 9 . .
8 3 . . 9 . 4 . 1
9 . . . 1 . . . 3

[1, 9, 4, 7, 8, 5, 6, 3, 2]
[3, 5, 8, 2, 6, 9, 1, 7, 4]
[2, 6, 7, 3, 4, 1, 5, 8, 9]
[2, 7, 1, 5, 4, 3, 8, 6, 9]
[9, 4, 3, 7, 8, 6, 5, 1, 2]
[6, 5, 8, 1, 9, 2, 7, 3, 4]
[4, 1, 7, 3, 2, 8, 9, 5, 6]
[8, 3, 5, 6, 9, 7, 4, 2, 1]
[9, 2, 6, 4, 1, 5, 8, 7, 3]

for _ 1 iteration time = 412 seconds 
for _ 2 or more iteration
--- 0.7158951759338379 seconds ---
[{1}, {9}, {4}, {7}, {8}, {5}, {6}, {3}, {2}]
[{3}, {5}, {8}, {2, 6}, {2, 6}, {9}, {1}, {7}, {4}]
[{2}, {6}, {7}, {3}, {4}, {1}, {5}, {8}, {9}]
[{2}, {7}, {1}, {5}, {4}, {3}, {8}, {6}, {9}]
[{9}, {4}, {3, 5}, {7}, {8}, {6}, {2, 5}, {1}, {2, 3, 5}]
[{6}, {3, 5}, {8}, {1}, {9}, {2}, {7}, {3, 5}, {4}]
[{4}, {1}, {6, 7}, {3}, {2}, {8}, {9}, {5}, {6, 7}]
[{8}, {3}, {2, 5}, {5, 6}, {9}, {7}, {4}, {2, 6}, {1}]
[{9}, {2, 7}, {5, 6}, {4}, {1}, {5, 6}, {8}, {2, 7}, {3}]

for _ 2 --- 0.009021997451782227 seconds ---
Number of wrong attempts:  72

for _ 1 --- 0.013039112091064453 seconds ---
Number of wrong attempts:  137

[[0, 9, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 3, 0, 0, 6, 0, 9, 0],
[0, 6, 0, 0, 1, 0, 0, 0, 4],
[4, 1, 0, 8, 3, 0, 9, 0, 0],
[0, 0, 8, 0, 9, 0, 0, 1, 0],
[0, 0, 0, 4, 0, 0, 0, 0, 3]]

..
. 9 . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . 3 . 6 .
. . . . . 6 . 1 .
. . . . 9 . . . 4
4 1 . . . 8 . . .
8 3 . . 9 . 4 . .
9 . . . 1 . . . 3

Rotated-
9 . . . 1 . . . 3
8 3 . . 9 . 4 . .
4 1 . . . 8 . . .
. . . . 9 . . . 4
. . . . . 6 . 1 .
. . . . . 3 . 6 .
. . . . . . . . .
. . . . . . . . .
. 9 . . . . . . .

--- 657.9697334766388 seconds ---
Number of wrong attempts:  15235417
from solutions---------------------------------------
[1, 9, 2, 3, 5, 4, 6, 8, 7]
[3, 4, 5, 6, 7, 8, 1, 2, 9]
[8, 6, 7, 1, 2, 9, 3, 4, 5]
[2, 7, 1, 5, 4, 3, 8, 6, 9]
[9, 5, 4, 7, 8, 6, 2, 1, 3]
[6, 3, 8, 2, 9, 1, 5, 7, 4]
[4, 1, 6, 7, 3, 8, 9, 2, 5]
[8, 3, 7, 5, 9, 2, 4, 6, 1]
[9, 5, 2, 4, 1, 6, 7, 8, 3]

'''