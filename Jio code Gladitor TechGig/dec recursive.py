import time
cord = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]


def main():
	# global path
	# global count
	# global matrix
	# global inform0
	# global inform1
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
	inform0 = [[[] for i in range(8)] for j in range(8)]
	inform1 = [[[] for i in range(8)] for j in range(8)]

	alternate = False
	# parent_index = 0
	for index in range(1, path_size):
		for i in range(8):
			for j in range(8):  # index-1 is parent index(inner index)
				if index - 1 in path_char.get(matrix[i][j], []):
					# print('for i and j:', i, j, 'index:', index)
					if index is 1:
						for num in range(8):
							x = i + cord[num][0]
							y = j + cord[num][1]
							# print('direction:', num, 'x, y:', x, y)
							if 0 <= x < 8 and 0 <= y < 8 and index in path_char.get(matrix[x][y], []):
								# print('Im in')
								inform0[x][y].append({(i, j)})
					elif index < path_size-1:
						for num in range(8):
							x = i + cord[num][0]
							y = j + cord[num][1]
							# print('direction:', num, 'x, y:', x, y)
							if 0 <= x < 8 and 0 <= y < 8 and index in path_char.get(matrix[x][y], []):
								# print('Im in')
								if alternate:
									for current_path in inform0[i][j]:
										if (x, y) not in current_path:
											ano = current_path.copy()
											ano.add((i, j))
											inform1[x][y].append(ano)
								else:
									for current_path in inform1[i][j]:
										# print(current_path)
										if (x, y) not in current_path:
											ano = current_path.copy()
											ano.add((i, j))
											inform0[x][y].append(ano)
											# print("Inside for Loop", 'Index:', index, 'cord', (x, y), inform0[x][y])
					else:
						for num in range(8):
							x = i + cord[num][0]
							y = j + cord[num][1]
							# print('direction:', num, 'x, y:', x, y)
							if 0 <= x < 8 and 0 <= y < 8 and index in path_char.get(matrix[x][y], []):
								# print('Im in')
								if alternate:
									for current_path in inform0[i][j]:
										if (x, y) not in current_path:
											# current_path.add((i, j))
											# ano = current_path.copy()
											# ano.add((x, y))
											# print('Path Number:', count+1, ano)
											count += 1
								else:
									for current_path in inform1[i][j]:
										if (x, y) not in current_path:
											# current_path.add((i, j))
											# ano = current_path.copy()
											# ano.add((x, y))
											# print('Path Number:', count+1, ano)
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

5
aaaaa
aaaaaaaa
aaaaaaaa
aaaaaaaa
aaaaaaaa
aaaaaaaa
aaaaaaaa
aaaaaaaa
aaaaaaaa
____
7
aaaaaaa
aaaaaaaa
aaaaaaaa
aaaaaaaa
aaaaaaaa
aaaaaaaa
aaaaaaaa
aaaaaaaa
aaaaaaaa
_____
4 a's
14196
--- 0.045118093490600586 seconds ---
5 a's
77016
--- 0.06216573715209961 seconds ---
6 a's
408764
--- 0.3800086975097656 seconds ---
Better up to length <=6
7 a's
2129440
--- 2.8505754470825195 seconds ---
___
8-as
10899404
--- 15.309681177139282 seconds ---

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
10899404
--- 16.292799472808838 seconds ---


'''