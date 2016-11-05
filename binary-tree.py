import queue

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

	def BFSbinary(self, value):
		que = queue.Queue()
		que.put(self)

		while que.qsize() > 0:
			val = que.get()

			if val.data == value:
				print(val.data)
			else:
				print(str(val.data), " ", end="")
				if val.left:
					que.put(val.left)
				if val.right:
					que.put(val.right)

	def DFSbinary(self,value):
		stack = [self]

		while len(stack) > 0:
			if stack[0].data == value:
				print(stack[0].value)
			else:
				print(str(stack[0].data), " ", end="")
				temp = stack.pop(0)
				if temp.right:
					stack.insert(0, temp.right)
				if temp.left:
					stack.insert(0, temp.left)




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

	def BFS(self, value):
		self.root.BFSbinary(value)

	def DFS(self, value):
		self.root.DFSbinary(value)

	

list = [1, 7, 4, 23, 8, 9, 4, 3, 5, 7, 9, 67, 6345, 324]
bst = BinarySearchTree()

bst.build_tree(list)
bst.inorder()
print()
bst.insert(500)
bst.inorder()
print()

bst.BFS(2)
print()

bst.DFS(2)