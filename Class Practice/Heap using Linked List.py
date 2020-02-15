class LinkedList:
	def __init__(self, value=None):
		self.value = value
		self.next = LinkedList() if value is not None else None

	def __str__(self):
		temp = self
		while temp.value is not None:
			print(temp.value, end=' <-')
			temp = temp.next
		return 'None'

	def add_element(self, new_element):
		if self.value is None:
			self.value = new_element
			self.next = LinkedList()
		elif self.value < new_element:
			if self.next is not None:
				new_node = LinkedList(self.value)
				new_node.next = self.next
				self.value = new_element
				self.next = new_node
			else:
				self.value = new_element
		else:
			self.next.add_element(new_element)

	def delete_max(self):
		max_value = None
		if self.value is not None:
			max_value = self.value
			if self.next is not None:
				self.value = self.next.value
				self.next = self.next.next
			else:
				self.value = None
		return max_value
