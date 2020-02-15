import time
cord = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]


def dodfs(index, visited, parent):
	global matrix
	global path
	global count
	global path_char
	global inform

	# if index in inform[parent[0]][parent[1]]:
	if index == len(path)-2:
		for next_step in inform[parent[0]][parent[1]][index]:
			if next_step not in visited:
				count += 1
		# print(count)
	else:
		for next_step in inform[parent[0]][parent[1]][index]:
			if next_step not in visited and index+1 in inform[next_step[0]][next_step[1]]:
				visited.append(next_step)
				dodfs(index+1, visited, next_step)

	visited.pop()


def main():
	global path
	global count
	global matrix
	global inform
	global path_char
	input()

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
		# print(inform[i])
	# Here information matrix is created

	for i in range(8):
		for j in range(8):
			if 0 in inform[i][j]:
				# print('i,j:', i, j, inform[i][j])
				visited = [(i, j)]  # Push operation
				index = 0
				parent = (i, j)
				dodfs(index, visited, parent)

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
____
4 a's
14196
--- 0.015037298202514648 seconds ---
5 a's
77016
--- 0.08120155334472656 seconds ---
6 a's
408764
--- 1.4087424278259277 seconds ---
Better above 6
7 a's
2129440
--- 2.536740779876709 seconds ---
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
--- 14.503556966781616 seconds ---

'''