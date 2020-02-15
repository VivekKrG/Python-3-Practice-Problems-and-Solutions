import time
cord = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]


def main():
	# global path
	# global count
	# global matrix
	# global inform0
	# global inform1
	# global inform
	# global path_char
	path_size = int(input())

	start_time = time.time()
	path = input()
	path_char = {}

	matrix = []
	for i in range(8):
		matrix.append(input())

	for index in range(len(path)):
		if path[index] in path_char:
			path_char[path[index]].append(index)
		else:
			path_char[path[index]] = [index]
	# print(path_char)

	count = 0
	# Making list of paths(set of coordinates) at every block of inform matrix
	inform = [[{} for i in range(8)] for j in range(8)]
	inform0 = [[[] for i in range(8)] for j in range(8)]
	inform1 = [[[] for i in range(8)] for j in range(8)]

	for i in range(8):
		for j in range(8):
			if matrix[i][j] in path_char:
				# print('for i and j:', i, j)
				for num in range(8):
					x = i + cord[num][0]
					y = j + cord[num][1]
					if 0 <= x < 8 and 0 <= y < 8:
						if matrix[x][y] in path_char:
							# print('in bound x,y:', x, y)
							# print('38:', 'matchar:', matrix[x][y],'returned list of index', path_char.get(matrix[x][y]))
							for index in path_char[matrix[i][j]]:
								if index == len(path) - 1:
									continue  # Need to put break
								# print('Inner index:', index, 'from', path_char[matrix[i][j]])
								for outer_index in path_char[matrix[x][y]]:
									# print('Outer Index:', outer_index, 'from', path_char[matrix[x][y]])
									if outer_index == index + 1:
										# print("Yes I'm in.")
										# print('Inform:', i, j, inform[i][j])
										if index in inform[i][j]:
											inform[i][j][index].append((x, y))
										else:
											inform[i][j][index] = [(x, y)]
										# print('Inform:', i, j, inform[i][j])
										break
	# print(inform)

	alternate = False
	# parent_index = 0
	for index in range(path_size):
		for i in range(8):
			for j in range(8):  # index-1 is parent index(inner index)
				if index in path_char.get(matrix[i][j], []):
					# print('for i and j:', i, j, 'index:', index)
					if index is 0 and 0 in inform[i][j]:
						for outer_cord in inform[i][j][0]:
							inform0[outer_cord[0]][outer_cord[1]].append({(i, j)})
							# print('for i and j:', i, j, 'index:', index, 'outer_cord:', outer_cord)
					elif index < path_size-2 and index in inform[i][j]:
						for outer_cord in inform[i][j][index]:
							if alternate:
								for current_path in inform0[i][j]:
									if (outer_cord[0], outer_cord[1]) not in current_path:
										ano = current_path.copy()
										ano.add((i, j))
										inform1[outer_cord[0]][outer_cord[1]].append(ano)
							else:
								for current_path in inform1[i][j]:
									# print(current_path)
									if (outer_cord[0], outer_cord[1]) not in current_path:
										ano = current_path.copy()
										ano.add((i, j))
										inform0[outer_cord[0]][outer_cord[1]].append(ano)
										# print("Inside for Loop", 'Index:', index, 'cord', (x, y), inform0[x][y])
					elif index in inform[i][j]:
						for outer_cord in inform[i][j][index]:
							if alternate:
								for current_path in inform0[i][j]:
									if (outer_cord[0], outer_cord[1]) not in current_path:
										count += 1
							else:
								for current_path in inform1[i][j]:
									if (outer_cord[0], outer_cord[1]) not in current_path:
										count += 1
		# for iter in range(8):
		# 	print('index: ', index, 'Row:', iter, inform1[iter]) if alternate else print('index: ', index, 'Row:', iter, inform0[iter])
		if alternate:
			inform0 = [[[] for i in range(8)] for j in range(8)]
		else:
			inform1 = [[[] for i in range(8)] for j in range(8)]
		alternate = not alternate

	# Here information matrix is created
	# for

	print(count)
	print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == '__main__':
	main()


'''
3
fit
fitfpoke
orlignom
ifefmart
tforarts
tekkenth
richieri
tintinti
pikachup

3
fit
fitfpoke
orlignom
ifefmirt
tforarfs
tekkenth
richieri
tintinti
pikachup

8
aaaaaaaa
aaaaaaaa
aaaaaaaa
aaaaaaaa
aaaaaaaa
aaaaaaaa
aaaaaaaa
aaaaaaaa
aaaaaaaa

___
4 a's
14196
--- 0.01604151725769043 seconds ---
5 a's
77016
--- 0.08420968055725098 seconds ---
6 a's
408764
--- 0.47322750091552734 seconds ---
7 a's
2129440
--- 3.296757459640503 seconds ---
___
8-as
10899404
--- 15.309681177139282 seconds ---

'''