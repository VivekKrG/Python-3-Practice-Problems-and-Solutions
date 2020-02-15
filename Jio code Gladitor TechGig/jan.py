import math

n, m = map(int, input().split())
boxes = list(map(int, input().split()))
man = list(map(int, input().split()))

man.sort()
boxes.sort()

same_wt = {man[0]: 1}
for i in range(1, len(man)):
	if man[i] == man[i-1]:
		same_wt[man[i]] += 1
	else:
		same_wt[man[i]] = 1
# print("man:", man)
# print("boxes:", boxes)

count = dict()
m_index = 0
b_index = 0
current_count = 0
while m_index < len(man):
	while b_index < len(boxes) and boxes[b_index] <= man[m_index]:
		current_count += 1
		b_index += 1
	count[man[m_index]] = count.get(man[m_index], current_count)
	current_count = 0
	# print(count)
	m_index += 1

for wt in count:
	count[wt] = math.ceil(count[wt]/same_wt[wt])

# print("Count:", count)
man.reverse()
# print(man)
time = -1
k = 1
for weight in man:
	if count[weight] > 0:
		present_max = math.ceil(count[weight]/k)
		time += 2*present_max
		# del count[weight]
		# print(count)
		for i in range(k, len(man)):
			count[man[i]] -= present_max
		# print(count, present_max, k, 'time:', time)
	elif k < len(man):
		present_neg = count[weight]
		count[man[k]] += present_neg
		# del count[weight]
		# print(count, present_neg, k, 'time:', time)
	k += 1

print(time)

'''
Traceback (most recent call last): 
File "CandidateCode.py", line 42,
in <module> count[man[k]] += present_neg KeyError: 32730

6 3
3 4 4 4 3 3
3 4 5 6 3 4

20 4
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
5 10 20 10

20 3
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
10 15 20

20 5
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
8 9 11 18 20

'''