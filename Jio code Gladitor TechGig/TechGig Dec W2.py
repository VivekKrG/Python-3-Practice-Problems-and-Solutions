def get_total(num):  # Num is string
	k = len(num)-1
	if k == 0:
		return int(num[0])//2
	if int(num[0]) % 2:
		print(num)
		return int('4'*k) + (10**k)*(int(num[0])//2)
	else:
		print(num)
		return int('4'*k) + (10**k)*(int(num[0])//2 - 1) + int(num[1:]) + 1


def main():
	tests = int(input())
	for __ in range(tests):
		left_side, right_side = input().split()
		total = get_total(right_side)
		left = get_total(left_side)

		if int(left_side[0]) % 2:
			print(total - left)
		else:
			print(total - left + 1)

main()

'''
4
1 99
44
12 120
40
10 452
193
200 5000
2400
'''