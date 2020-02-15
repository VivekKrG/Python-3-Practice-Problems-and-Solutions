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

	fill_inform()
	count = 0
	# print(my_matrix)  # Loop need to run from 11 to 88
	for i in range(11, 89):
		if 0 in inform[i]:
			parent = i
			index = 0
			visited = {i}
			stack = [i]
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
9 a : 54738536
--- 44.17640924453735 seconds --- inform[i][index] -> list of next i
9 a : 54738536
--- 43.23495173454285 seconds --- inform[i][index] -> with set
'''