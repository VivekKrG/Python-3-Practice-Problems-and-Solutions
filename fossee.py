arr = [1, 1, 2]


def fill_next():
	arr.append(arr[-1] + arr[-2])


def make_fibo(n):
	if n < 3:
		return
	else:
		for i in range(n - 3):
			fill_next()
		return


def fibo_sum(n):
	make_fibo(n)
	print(arr)
	return sum(arr)

print(fibo_sum(5))
