"""
This code us based on code which can be found on toodle.computing.dcu.ie - which helped me to
impliment the Node class and the beginning of the BST class.
"""
class Node:
	def __init__(self, item, left = None, right = None):
		self.item = item
		self.left = left
		self.right = right

class BST:
	def __init__(self):
		self.root = None

	def recursive_add(self,ptr,item):
		if ptr == None:
			return Node(item)
		elif item < ptr.item:
			ptr.left = self.recursive_add(ptr.left,item)
		elif item > ptr.item:
			ptr.right = self.recursive_add(ptr.right, item)
		return ptr

	def add(self, item):
		self.root = self.recursive_add(self.root,item)

	def recursive_search(self,ptr,item):
		if ptr == None:
			return False
		elif item == ptr.item:
			return True
		elif item < ptr.item:
			return self.recursive_search(ptr.left,item)
		else:
			return self.recursive_search(ptr.right,item)

	def search(self,item):
		return self.recursive_search(self.root, item)


	def print_pre_order(self):
		self.recursive_print_pre_order(self.root)


	def recursive_print_pre_order(self, ptr):
		if ptr == None:
			pass
		else:
			print(ptr.item)
			self.recursive_print_pre_order(ptr.left)
			self.recursive_print_pre_order(ptr.right)

	def print_in_order(self):
		self.recursive_print_in_order(self.root)

	def recursive_print_in_order(self, ptr):
		if ptr == None:
			pass
		else:
			self.recursive_print_in_order(ptr.left)
			print(ptr.item)
			self.recursive_print_in_order(ptr.right)

	def print_post_order(self):
		self.recursive_print_post_order(self.root)

	def recursive_print_post_order(self, ptr):
		if ptr == None:
			pass
		else:
			self.recursive_print_post_order(ptr.left)
			self.recursive_print_post_order(ptr.right)
			print(ptr.item)


if __name__ == "__main__":
	bst = BST()
	bst.add(10)
	bst.add(5)
	bst.add(20)
	bst.add(2)
	bst.add(8)

	bst.print_post_order()