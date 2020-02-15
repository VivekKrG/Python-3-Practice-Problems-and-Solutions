class Node:
	def __init__(self, key):
		self.key = key
		self.left = None
		self.right = None


class Tree:
	def __init__(self, initial_value=None):
		if initial_value:
			self.root = Node(initial_value)
		else:
			self.root = None

	def is_empty(self):
		return self.root is None

	def is_leaf(self):
		return Tree.helper_is_leaf(self.root)

	def height(self):
		if self.is_empty() is False:
			if self.is_leaf():
				return 0
			return Tree.helper_height(self.root, prev_height=1)
		else:
			return -1

	def minval(self):
		if self.is_empty():
			return
		else:
			return Tree.helper_minval(self.root)

	def maxval(self):
		if self.is_empty():
			return
		return Tree.helper_maxval(self.root)

	def inorder(self):
		# call helper method that should work on Node
		if self.root:
			return self.helper_inorder(self.root)
		else:
			return []

	def preorder(self):
		# call helper method that should work on Node
		if self.root:
			return self.helper_preorder(self.root)
		else:
			return []

	def postorder(self):
		# call helper method that should work on Node
		if self.root:
			return self.helper_postorder(self.root)
		else:
			return []

	def insert(self, value):
		if self.is_empty() is False:
			Tree.helper_insert(self.root, value)
		else:
			self.root = Node(value)

	def search(self, element):
		if self.root:
			return Tree.helper_search(self.root, element)
		else:
			return False

	def delete(self, element):
		if self.is_empty() is False:
			if self.is_leaf() and self.root.key == element:
				self.root = None
				return 1
			return Tree.helper_delete(self.root, element, self)
		else:
			return

	# Methods starting with "helper_" are made to play with instances of Class: Node.

	@staticmethod
	def helper_is_leaf(self):
		return self.left is None and self.right is None

	@staticmethod
	def helper_height(self, prev_height):
		if Tree.helper_is_leaf(self):
			return 0
		left_height = Tree.helper_height(self.left, 1) if self.left else 0
		right_height = Tree.helper_height(self.right, 1) if self.right else 0
		return max(left_height, right_height) + prev_height

	@staticmethod
	def helper_minval(self):
		if self.left is None:
			return self.key
		else:
			return Tree.helper_minval(self.left)

	@staticmethod
	def helper_maxval(self):
		if self.right is None:
			return self.key
		else:
			return Tree.helper_maxval(self.right)

	@staticmethod
	def helper_insert(self, value):
		if self.key >= value:
			if self.left:
				Tree.helper_insert(self.left, value)
			else:
				self.left = Node(value)
		else:
			if self.right:
				Tree.helper_insert(self.right, value)
			else:
				self.right = Node(value)

	# Following the instance method
	def helper_inorder(self, node):  # self is reference of Node type object
		if node:
			order = self.helper_inorder
			return order(node.left) + [node.key] + order(node.right)
		else:
			return []

	def helper_preorder(self, node):  # self is reference of Node type object
		if node:
			order = self.helper_preorder
			return [node.key] + order(node.left) + order(node.right)
		else:
			return []

	def helper_postorder(self, node):  # self is reference of Node type object
		if node:  # is to check leaf nodes= print(node.key, 'is leaf:', Tree.helper_is_leaf(node))
			order = self.helper_postorder
			return order(node.left) + order(node.right) + [node.key]
		else:
			return []

	@staticmethod
	def helper_search(self, element):
		if self:
			if self.key == element:
				return True
			elif self.key > element:
				return Tree.helper_search(self.left, element)
			else:
				return Tree.helper_search(self.right, element)
		else:
			return False

	@staticmethod
	def helper_delete(self, element, parent):
		if element < self.key and self.left is not None:
			return Tree.helper_delete(self.left, element, self)
		elif element > self.key and self.right is not None:
			return Tree.helper_delete(self.right, element, self)
		elif element == self.key:
			if Tree.helper_is_leaf(self):
				if parent.left and parent.left.key == element:
					parent.left = None
				else:
					parent.right = None
			elif self.left is None:  # Left subtree is empty
				self.key = self.right.key
				self.left = self.right.left
				self.right = self.right.right
			else:
				max_element_of_left_sub_tree = Tree.helper_maxval(self.left)
				self.key = max_element_of_left_sub_tree
				Tree.helper_delete(self.left, max_element_of_left_sub_tree, self)
			return 1
		else:
			return 0


def fill_tree(treee, number_of_elements, min_val, max_val):
	import random
	for _ in range(number_of_elements):
		treee.insert(random.randint(min_val, max_val))


def delete_elements(treee, number_of_elements, min_val, max_val):
	import random
	count = 0
	while count is not number_of_elements and not treee.is_empty():
		count += treee.delete(random.randint(min_val, max_val))


if __name__ == '__main__':
	'''
	tree = Tree(8)
	tree.insert(5)
	tree.insert(7)
	tree.insert(10)
	tree.insert(9)
	tree.insert(1)
	tree.insert(0)
	tree.insert(2)
	tree.insert(6)
	tree.insert(7.5)
	tree.insert(15)
	'''
	'''
	Tree:tree	8
			  /   \
			5      10
		  /   \    / \
		 1     7  9  15
		/ \   / \
	   0   2 6  7.5
	'''
	'''
	print('Inoreder:', tree.inorder())
	print('Preorder:', tree.preorder())
	print('Postorder', tree.postorder())
	print('5 is present:', tree.search(5))
	print('1 is present:', tree.search(1))
	print('9 is present:', tree.search(9))
	print('10 is present:', tree.search(10))
	print('51 is present:', tree.search(51))
	print('0 is present:', tree.search(0))
	print('7 is present:', tree.search(7))

	print('"tree" is Empty:', tree.is_empty())
	print('Minimum value in "tree":', tree.minval())
	print('Maximum value in "tree":', tree.maxval())

	print('Height of "tree":', tree.height())

	tree.delete(5)
	print('Deleted 5:', tree.inorder(), tree.preorder(), tree.postorder())
	tree.delete(8)
	print('Deleted 8:', tree.inorder(), tree.preorder(), tree.postorder())
	print('Height of "tree":', tree.height())

	tree.delete(9)
	print('Deleted 9:', tree.inorder(), tree.preorder(), tree.postorder())
	print('Height of "tree":', tree.height())
	tree.delete(7)
	print('Deleted 7:', tree.inorder(), tree.preorder(), tree.postorder())
	print('Height of "tree":', tree.height())
	tree.delete(7.5)
	print('Deleted 7.5:', tree.inorder(), tree.preorder(), tree.postorder())
	print('Height of "tree":', tree.height())

	tr = Tree(2)
	print('Height of "tr":', tr.height())
	print(tr.inorder())
	tr.delete(1)
	tr.delete(4)
	tr.delete(2)
	print(tr.inorder())
	print('Height of "tr":', tr.height())

	'''
	# ------------------------ #
	import time
	start = time.time()
	tree2 = Tree()
	fill_tree(tree2, 5000, 0, 1000)
	print('Height of "tree2":', tree2.height())
	tree2.inorder()
	tree2.preorder()
	tree2.postorder()
	# print(tree2.inorder())
	# print(tree2.preorder())
	# print(tree2.postorder())

	delete_elements(tree2, 500, 0, 1000)
	# print(tree2.inorder())
	print('Height of "tree2":', tree2.height())
	print("--- %s seconds ---" % (time.time() - start))



