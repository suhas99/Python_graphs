class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

	def insert(self, data):
		if self.data:
			if data < self.data:
				if self.left is None:
					self.left = Node(data)
				else:
					self.left.insert(data)
			elif data > self.data:
				if self.right is None:
					self.right = Node(data)
				else:
					self.right.insert(data)
		else:
			self.data = data


	def height(self, root):
		if root is None:
			return 0
		return max(self.height(root.left), self.height(root.right)) + 1

	def is_balanced(self, root):
		if root is None:
			return True
		lh = self.height(root.left)
		rh = self.height(root.right)

		if abs(lh - rh) <= 1 and self.is_balanced(root.left) is True and self.is_balanced(root.right) is True:
			return True
		return False


root = Node(6)
root.insert(10)
root.insert(3)
root.insert(11)
root.insert(9)
root.insert(18)
root.insert(4)


if root.is_balanced(root):
	print("Balanced stuff")
else:
	print("Not a balanced stuff")
