# Use input() to read input from STDIN and use print to write your output to STDOUT


class Myq:
	def __init__(self, p):
		self.arr = []
		self.front = 0
		self.last = -1
		self.counter = 0
		self.summ = p

	def head(self):
		return self.arr[self.front]

	def reset(self):
		self.arr = []
		self.front = 0
		self.last = -1

	def put(self, order):
		if order == self.summ:
			self.counter += 1
			self.reset()
		elif order < self.summ:
			# print('I am here order < summ')
			self.arr.append(order)
			self.last += 1

			while self.front < self.last and self.head() + order > self.summ:
				self.front += 1

			if self.front < self.last:
				if self.head() + order == self.summ:
					self.count_increment()
				i = self.front
				while i < self.last:
					self.arr[i] += order
					i += 1
		else:
			self.reset()

	def count_increment(self):
		self.counter += 1
		self.arr = self.arr[self.front+1:self.last+1]
		self.last = self.last - self.front-1
		self.front = 0


def main():
	tests = int(input())
	for _ in range(tests):
		n, p = map(int, input().split())
		string = input()
		myq = Myq(p)
		for char in string:
			myq.put(ord(char) - 96)
			# print(myq.front, myq.arr, myq.last, 'count:', myq.counter)

		print(myq.counter)


main()

'''
2
5 4
abdca
3 1
bcd
Output
2
0


2
10 12
abdcadaaaaaaaaaaaaaalaamaaabbbababcaca
3 1
bcd

'''
