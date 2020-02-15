class PriorityQueue:
	def __init__(self, initial_value=None):
		self.arr = [initial_value] if initial_value is not None else None
		self.size = None

	def __str__(self):
		return str(self.arr)

	def add_element(self, new_value):
		if self.arr is None:
			self.arr = [new_value]
		else:
			self.arr.append(new_value)
			child_index = len(self.arr)-1

			while child_index > 0 and self.arr[child_index] > self.arr[(child_index-1)//2]:
				(self.arr[child_index], self.arr[(child_index-1)//2]) = (self.arr[(child_index-1)//2], self.arr[child_index])
				child_index = (child_index-1)//2
		self.size = len(self.arr)

	def get_max(self):
		if not self.arr:
			return None
		(self.arr[0], self.arr[self.size-1]) = (self.arr[self.size-1], self.arr[0])
		# max_val = self.arr.pop()
		self.size = self.size-1
		self.heapify(0)
		return self.arr[self.size]

	def heapify(self, index):
		if self.size is None:
			self.size = len(self.arr)

		left = 2 * index + 1
		right = left + 1

		if right > self.size-1 and index >= self.size//2 - 1:
			if left < self.size and self.arr[index] < self.arr[2*index+1]:
				(self.arr[index], self.arr[2*index+1]) = (self.arr[2*index+1], self.arr[index])
			return

		smaller = left if self.arr[left] >= self.arr[right] else right  # getting child which is max
		(self.arr[index], self.arr[smaller]) = (self.arr[smaller], self.arr[index])
		self.heapify(smaller)

	def heap_sort(self):
		self.size = len(self.arr)
		for i in range(len(self.arr)):
			self.get_max()
		print(self.arr)
