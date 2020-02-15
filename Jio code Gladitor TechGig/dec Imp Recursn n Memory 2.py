import time
cord = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]


def dodfs(index, visited, parent, stack):
	global path
	global count
	global matrix
	global inform
	global inform0
	global inform1
	global path_char
	global path_size

	# if index in inform[parent[0]][parent[1]]:
	if index == path_size-2:
		for next_step in inform[parent[0]][parent[1]][index]:
			if next_step not in visited:
				count += 1
		# print(count)
	else:
		for next_step in inform[parent[0]][parent[1]][index]:
			if next_step not in visited and index+1 in inform[next_step[0]][next_step[1]]:
				visited.add(next_step)
				stack.append(next_step)
				dodfs(index+1, visited, next_step, stack)
		if not stack:
			return
	visited.remove(stack.pop())


def main():
	global path
	global count
	global matrix
	global inform
	global inform0
	global inform1
	global path_char
	global path_size
	path_size = int(input())

	start_time = time.time()
	path = input()
	path_char = {}

	matrix = []
	for i in range(8):
		matrix.append(input())

	for index in range(path_size):
		if path[index] in path_char:
			path_char[path[index]].append(index)
		else:
			path_char[path[index]] = [index]
	# print(path_char)

	count = 0
	inform0 = [[[] for i in range(8)] for j in range(8)]  # inform1[][]-> gives list of all paths
	inform1 = [[[] for i in range(8)] for j in range(8)]

	alternate = False
	# parent_index = 0
	for index in range(1, 5):
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
					elif index <= path_size-2 and index < 4:  # path_size - 1:
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
					elif path_size <= 5:
						for num in range(8):
							x = i + cord[num][0]
							y = j + cord[num][1]
							# print('direction:', num, 'x, y:', x, y)
							if 0 <= x < 8 and 0 <= y < 8 and index in path_char.get(matrix[x][y], []):
								# print('Im in')
								if alternate:
									for current_path in inform0[i][j]:
										if (x, y) not in current_path:
											count += 1
								else:
									for current_path in inform1[i][j]:
										if (x, y) not in current_path:
											count += 1
					else:
						break
			else:
				continue
			break
		else:
			# for iter in range(8):
			# 	print('index: ', index, 'Row:', iter, inform1[iter]) if alternate else print('index: ', index, 'Row:', iter, inform0[iter])
			if alternate:
				inform0 = [[[] for i in range(8)] for j in range(8)]
			else:
				inform1 = [[[] for i in range(8)] for j in range(8)]
			alternate = not alternate
			continue
		break

	# print(inform0)
	# print(inform1)
	if count:
		print(count, 'from if count')
		print("--- %s seconds ---" % (time.time() - start_time))
		return

	inform = [[{} for i in range(8)] for j in range(8)]
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
								if index == path_size - 1:
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
		# print(inform[i])
	# Here information matrix is created

	# Use inform0 matrix: inform0[][] gives list of all paths up to index 4 -> path is set of coordinates
	# print(inform1)
	for i in range(8):
		for j in range(8):
			for current_path in inform0[i][j]:
				# print('i,j:', i, j, inform[i][j])
				visited = current_path.copy()
				visited.add((i, j))  # Push operation
				stack = []
				index = 3
				parent = (i, j)
				dodfs(index, visited, parent, stack)

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

6
aaaaaa
aaaaaaaa
aaaaaaaa
aaaaaaaa
aaaaaaaa
aaaaaaaa
aaaaaaaa
aaaaaaaa
aaaaaaaa

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
____
4 a's
14196
--- 0.015037298202514648 seconds ---
5 a's
77016 from if count
--- 0.06116151809692383 seconds ---
6 a's
408764
--- 0.40006041526794434 seconds ---
Better above 6
7 a's
2129440
--- 2.0674920082092285 seconds ---
___
8-as only stack as visited
10899404
--- 14.194271087646484 seconds ---

9
aaaaaaaaa
aaaaaaaa
aaaaaaaa
aaaaaaaa
aaaaaaaa
aaaaaaaa
aaaaaaaa
aaaaaaaa
aaaaaaaa

___
8 a's with stack and set() both
10899404
--- 10.189078330993652 seconds ---
9 a's
54738536
--- 50.549904346466064 seconds ---

9
aaaaaaaaa
aaaaaaaa
aaaaaaaa
aaaaaaaa
aaabaaaa
aaaaaaaa
aaaaaaaa
aaaaaaaa
aaaaaaaa

'''