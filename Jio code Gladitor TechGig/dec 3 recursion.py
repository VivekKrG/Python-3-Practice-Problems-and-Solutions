import time
cord = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]


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

input()
path = input()
start_time = time.time()
matrix = []
for i in range(8):
	matrix.append(input())

count = 0
for i in range(8):
	for j in range(8):
		if matrix[i][j] == path[0]:
			visited_x = [(i, j)]  # Push operation
			index_x = 1
			parent_x = (i, j)
			dodfs(index_x, visited_x, parent_x)


print(count)
print("--- %s seconds ---" % (time.time() - start_time))


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

5
fitti
fitfpoke
orlignom
ifefmart
tforafts
tikkenth
richieri
tiftifti
pikachup

8


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

3
abc
abcabcab
abcabcab
abcabcab
abcabcab
abcabcab
abcabcab
abcabcab
abcabcab

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
7 a's
2129440
--- 7.536024808883667 seconds ---
____
10899404
--- 40.32271599769592 seconds ---

'''