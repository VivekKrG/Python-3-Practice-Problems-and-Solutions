n, m = map(int, input().split())
if n == 1 and m == 1:
	print(0)
else:
	for row in range(1, n+1):
		# print('hello bro', row)
		for col in range(n+1, n+m+1):
			print(row*col, end=' ')
		print()
