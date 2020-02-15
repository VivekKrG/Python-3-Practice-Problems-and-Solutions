def check_compo(any_num):
	for i in range(2, int(any_num**0.5)+1):
		if any_num % i == 0:
			return True

	return False


num = int(input())
compo = 6

while True:
	b = num+compo
	if check_compo(b):
		print(b, compo)
		break
	else:
		compo += 1
		while check_compo(compo) is not True:
			compo += 1
