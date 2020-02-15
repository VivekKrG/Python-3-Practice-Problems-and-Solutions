n, m = map(int, input().split())
a_elem = map(int, input().split())
b_elem = map(int, input().split())
b_dict = dict()
a_dict = dict()
for elem in b_elem:
	b_dict[elem] = 1 + b_dict.get(elem, 0)

# print(b_dict)
for elem in a_elem:
	a_dict[elem] = 1 + a_dict.get(elem, 0)

# print(a_dict)
if a_dict == b_dict:
	print(0)
else:
	x = 0
	for x in range(1, m):
		for item in a_dict:
			new = (item + x) % m
			if new in b_dict:
				b_dict[new] -= a_dict[item]
				if b_dict[new] == 0:
					del b_dict[new]
				elif b_dict[new] < 0:
					break
		else:
			if b_dict:
				continue
			print(x)
			break


'''
4 3
0 0 2 1
2 0 1 1

1

5 10
0 0 0 1 2
2 1 0 0 0

0

3 2
0 0 0
1 1 1

1
'''