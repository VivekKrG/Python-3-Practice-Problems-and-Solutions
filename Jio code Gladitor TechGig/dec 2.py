cord = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

'''
def dodfs(index, visited, parent):
	global matrix
	global path
	global count
	for num in range(8):
		x = parent[0]+cord[num][0]
		y = parent[1]+cord[num][1]
		if 0 <= x < 8 and 0 <= y < 8:
			if (x, y) not in visited:
				if matrix[x][y] == path[index]:
					if index == len(path)-1:
						count += 1
						# print(visited, (x, y), count)
					else:
						visited.append((x, y))
						dodfs(index+1, visited, (x, y))

	visited.pop()
'''

input()
path = input()
matrix = []
for i in range(8):
	matrix.append(input())

count = 0
for i in range(8):
	for j in range(8):
		if matrix[i][j] == path[0]:
			visited = [(i, j)]  # Push operation
			index = 1
			parent = (i, j)
			# dodfs(index, visited, parent)

			start = 0
			pre = []
			check = 0
			for around in range(8):
				while True:
					# print('inside while', parent)
					for num in range(start, 8):
						x = parent[0] + cord[num][0]
						y = parent[1] + cord[num][1]
						if 0 <= x < 8 and 0 <= y < 8:
							if (x, y) not in visited:
								# print('for', parent, (x, y), visited, index, num)
								# print(matrix[x][y], path[index], index)
								if matrix[x][y] == path[index]:
									if index == len(path) - 1:
										count += 1
										# print(visited, (x, y), count, 'pre=', pre, index, check)
									else:
										visited.append((x, y))
										parent = (x, y)
										index += 1
										# start = 0
										break
					else:
						visited.pop()
						index -= 1
						if len(visited) > 1:
							parent = visited[-1]
							start = pre.pop()[0]+1
						else:
							# print('Breaking', parent, index)
							break


print(count)


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
Output
5

3
fitti
fitfpoke
orlignom
ifefmart
tforafts
tikkenth
richieri
tiftifti
pikachup

7


3
fit
fitfpoke
orlignom
ifefmarf
tforarts
tekkenth
richieri
tintinti
pikachup

3
fitti
  012345678
0 fitfpoke
1 orlignom
2 ifefmart
3 tforafts
4 tikkenth
5 richieri
6 tiftifti
7 pikachup

[(2, 1), (2, 0), (3, 0), (4, 0)] (4, 1) 1 pre= [6, 4, 4]
[(2, 1), (2, 0), (3, 0), (4, 0)] (5, 1) 2 pre= [6, 4, 4]
[(3, 1), (4, 1), (4, 0), (3, 0)] (2, 0) 3 pre= [4, 6, 0]
[(3, 1), (4, 1), (3, 0), (4, 0)] (5, 1) 4 pre= [4, 7, 4]
4

'''