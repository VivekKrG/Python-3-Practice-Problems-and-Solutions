tests = int(input())
# for __ in range(tests):
sums = list(map(int, input().split()))
for given in sums:
	if given < 15:
		print("NO")
		continue
	remain = given % 14
	if 1 <= remain <= 6:
		print("YES")
	else:
		print('NO')

'''
4
29 34 19 38

YES
YES
YES
NO

'''