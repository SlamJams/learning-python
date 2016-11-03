class Node(object):
	def __init__(self, data = None):
		self.data = data
		self.left = None
		self.right = None

	def insert(self, data):
		
		if self.data > data:
			if self.left:
				self.left.insert(data)
			else:
				self.left = Node(data)

		elif self.data < data:
			if self.right:
				self.right.insert(data)
			else:
				self.right = Node(data)
		else:
			self.data == data

	def inorder(self):
		if self:
			if self.left:
				self.left.inorder()

			print(str(self.data), " ", end="")

			if self.right:
				self.right.inorder()


class BinarySearchTree(object):
	def __init__(self):
		self.root = None

	def get_root(self):
		 self.root

	def build_tree(self, list):
		for x in list:
			self.insert(x)


	def insert(self, data):
		if self.root:
			 self.root.insert(data)
		else:
			self.root = Node(data)

	def inorder(self):
		self.root.inorder()


	

list = [1, 7, 4, 23, 8, 9, 4, 3, 5, 7, 9, 67, 6345, 324]
bst = BinarySearchTree()

bst.build_tree(list)
bst.inorder()
print()
bst.insert(500)
bst.inorder()
print()