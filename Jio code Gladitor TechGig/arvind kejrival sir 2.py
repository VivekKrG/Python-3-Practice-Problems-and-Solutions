import time
circle = [-1, -11, -10, -9, 1, 11, 10, 9]


# dodfs(parent, index, visited, stack)
def dodfs(parent, index, visited, stack):
	global count

	if index == path_size-2:
		for next_step in inform[parent][index]:
			if next_step not in visited:
				count += 1
		# print(count)
	else:
		for next_step in inform[parent][index]:
			if next_step not in visited and index+1 in inform[next_step]:
				# print(next_step, visited, stack, type(next_step))
				visited.add(next_step)
				stack.append(next_step)
				dodfs(next_step, index+1, visited,  stack)
		if not stack:
			return
	visited.remove(stack.pop())


def fill_inform():
	global inform
	inform = [{} for i in range(100)]
	for i in range(11, 89):
		if my_matrix[i] in path_char:
			for index in path_char[my_matrix[i]]:
				for direction in circle:
					x = i + direction
					if my_matrix[x] in path_char:
						if index == path_size - 1:
							continue
						for outer_index in path_char[my_matrix[x]]:
							if outer_index == index + 1:
								if index in inform[i]:
									inform[i][index].add(x)
								else:
									inform[i][index] = {x}
								break
	# print(inform)


def main():
	global path_size
	global path
	global my_matrix
	global count
	global inform
	global path_char

	path_size = int(input())
	start_time = time.time()
	path = input()
	path_char = {}

	for index in range(path_size):
		if path[index] in path_char:
			path_char[path[index]].append(index)
		else:
			path_char[path[index]] = [index]

	my_matrix = '0'*10
	for i in range(8):
		my_matrix += '0' + input() + '0'
	my_matrix += '0'*10

	count = 0
	inform0 = [[] for i in range(100)]  # inform1[][]-> gives list of all paths
	inform1 = [[] for j in range(100)]

	alternate = False
	# parent_index = 0
	for index in range(1, 5):
		for i in range(11, 89):
			if index - 1 in path_char.get(my_matrix[i], []):
				# print('for i and j:', i, j, 'index:', index)
				if index is 1:
					for num in circle:
						x = i + num
						if index in path_char.get(my_matrix[x], []):
							# print('Im in')
							inform0[x].append({i})
				elif index <= path_size - 2 and index < 4:  # path_size - 1:
					for num in circle:
						x = i + num
						if index in path_char.get(my_matrix[x], []):
							# print('Im in')
							if alternate:
								for current_path in inform0[i]:
									if x not in current_path:
										ano = current_path.copy()
										ano.add(i)
										inform1[x].append(ano)
							else:
								for current_path in inform1[i]:
									# print(current_path)
									if x not in current_path:
										ano = current_path.copy()
										ano.add(i)
										inform0[x].append(ano)
						# print("Inside for Loop", 'Index:', index, 'cord', (x, y), inform0[x][y])
				elif path_size <= 5:
					for num in circle:
						x = i + num
						if index in path_char.get(my_matrix[x], []):
							# print('Im in')
							if alternate:
								for current_path in inform0[i]:
									if x not in current_path:
										count += 1
							else:
								for current_path in inform1[i]:
									if x not in current_path:
										count += 1
				else:
					break
		else:
			if alternate:
				inform0 = [[] for i in range(100)]
			else:
				inform1 = [[] for i in range(100)]
			alternate = not alternate
			continue
		break

	if count:
		print(count, 'from if count')
		print("--- %s seconds ---" % (time.time() - start_time))
		return

	fill_inform()
	# print(my_matrix)  # Loop need to run from 11 to 88
	for i in range(11, 89):
		for current_path in inform0[i]:
			visited = current_path.copy()
			visited.add(i)  # Push operation
			stack = []
			index = 3
			parent = i
			dodfs(parent, index, visited, stack)

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

4 a : 14196 inform[i][index] -> list of next i
--- 0.03509235382080078 seconds ---

8 a :10899404
--- 8.455467700958252 seconds ---
9 a : 54738536
--- 44.17640924453735 seconds --- inform[i][index] -> list of next i
9 a : 54738536
--- 43.23495173454285 seconds --- inform[i][index] -> with set
'''