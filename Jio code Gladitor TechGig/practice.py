''' Read input from STDIN. Print your output to STDOUT '''


# Use input() to read input from STDIN and use print to write your output to STDOUT
def check(matrix):
	temp = 1
	for i in range(len(matrix)):
		temp = min(matrix[i])
		if temp == 0:
			break
	return temp


def main():
	n, m = map(int, input().split())
	matrix = []
	fire = 0
	for i in range(n):
		row = list(map(int, input().split()))
		if fire == 0:
			fire = max(row)
		matrix.append(row)

	if fire == 0:
		print(-1, end='')
		return
	if check(matrix):
		print(0, end='')
		return

	count = 0
	new_mat = [[0 for j in range(m)] for i in range(n)]

	while True:
		for i in range(n):
			for j in range(m):
				if i:
					if i < n - 1:
						if j:
							if j < m - 1:
								new_mat[i][j] = max(matrix[i][j], matrix[i - 1][j], matrix[i + 1][j], matrix[i][j - 1],
								                    matrix[i][j + 1])
							else:
								new_mat[i][j] = max(matrix[i][j], matrix[i - 1][j], matrix[i + 1][j], matrix[i][j - 1])
						elif m - 1:
							new_mat[i][j] = max(matrix[i][j], matrix[i - 1][j], matrix[i + 1][j], matrix[i][j + 1])
						else:
							new_mat[i][j] = max(matrix[i][j], matrix[i - 1][j], matrix[i + 1][j])
					else:
						if j:
							if j < m - 1:
								new_mat[i][j] = max(matrix[i][j], matrix[i - 1][j], matrix[i][j - 1], matrix[i][j + 1])
							else:
								new_mat[i][j] = max(matrix[i][j], matrix[i - 1][j], matrix[i][j - 1])
						elif m - 1:
							new_mat[i][j] = max(matrix[i][j], matrix[i - 1][j], matrix[i][j + 1])
						else:
							new_mat[i][j] = max(matrix[i][j], matrix[i - 1][j])
				elif n - 1:
					if j:
						if j < m - 1:
							new_mat[i][j] = max(matrix[i][j], matrix[i + 1][j], matrix[i][j - 1], matrix[i][j + 1])
						else:
							new_mat[i][j] = max(matrix[i][j], matrix[i + 1][j], matrix[i][j - 1])
					elif m - 1:
						new_mat[i][j] = max(matrix[i][j], matrix[i + 1][j], matrix[i][j + 1])
					else:
						new_mat[i][j] = max(matrix[i][j], matrix[i + 1][j])

				else:
					if j:
						if j < m - 1:
							new_mat[i][j] = max(matrix[i][j], matrix[i][j - 1], matrix[i][j + 1])
						else:
							new_mat[i][j] = max(matrix[i][j], matrix[i][j - 1])
					elif m - 1:
						new_mat[i][j] = max(matrix[i][j], matrix[i][j + 1])
					else:
						new_mat[i][j] = matrix[i][j]

		# print(new_mat[i])

		count += 1
		if check(new_mat):
			break
		del matrix
		matrix = new_mat[:]
		del new_mat
		new_mat = [[0 for j in range(m)] for i in range(n)]
	# print(id(new_mat), id(matrix))

	print(count, end='')


main()

