



class Node(object):
	def __init__(self, data = None, left = None, right = None):
		self.data = data
		self.left = left
		self.right = right

	def insert(self, data):
		if self.value == data:
			return False
		elif self.value > data:
			if self.leftChild:
				return self.leftChild.insert(data)
			else:
				self.leftChild = Node(data)
				return True

		else:
			if self.rightChild:
				return self.rightChild.insert(data)
			else:
				self.rightChild = Node(data)
				return True



class BinarySearchTree(object):
	def __init__(self, root = None):
		self.root = root

	def get_root(self):
		return self.root

	def insert(self, item):
		if self.root:
			return self.root.insert(data)
		else:
			self.root = Node(data)
			return True

	def search(self, node, item):
