odd = 0


def get_total(num):
	global odd

	if num < 20:
		if num > 9:
			odd = 1
			return 4
		else:
			odd = num%2
			return num//2
	else:
		given = num
		count = 4
		num //= 10
		k = 1
		while num:
			rem = num % 10
			odd = rem % 2
			num //= 10
			if num:
				count += 4*10**k
			else:
				if odd:
					count += (rem // 2) * 10 ** k
				else:
					count += (rem//2 - 1) * 10 ** k + (given % (10**k))+1
			# print('num=', num, 'given =', given, 'k =', k, 'count =', count)
			k += 1
		return count


def main():
	tests = int(input())
	for __ in range(tests):
		left_side, right_side = map(int, input().split())
		total = get_total(right_side)
		left = get_total(left_side)

		# print(total, left)
		if odd:
			print(total - left)
		else:
			print(total - left+1)


main()