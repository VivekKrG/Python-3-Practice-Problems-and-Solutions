tests = int(input())
for __ in range(tests):
	digits = input()
	count_digit = dict()
	for digit in digits:
		count_digit[digit] = 1 + count_digit.get(digit, 0)

	if count_digit.get('0', 0) is 0:
		print('cyan')
	else:
		count_digit['0'] -= 1
		# for divisibility of 2
		even_present = 0
		sum = 0
		for item in count_digit:
			sum += int(item) * count_digit.get(item, 0)
			if even_present is 0 and int(item) % 2 is 0 and count_digit.get(item, 0):
				even_present = 1

		if sum % 3 is 0 and even_present:
			print('red')
		else:
			print('cyan')
'''
red
red
cyan
cyan
cyan
red

'''