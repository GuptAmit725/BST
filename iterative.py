class node:
	def __init__(self,info):
		self.info = info
		self.left = None
		self.right = None

class BST:
	def buildBST(self, root, ele):
		curr = root
		temp = None
		if root == None:
			return node(ele)
		while curr:
			temp = curr
			if ele < temp.info:
				temp = temp.left
			else:
				temp = temp.right
		if ele < temp:
			temp.left = node(ele)
		else:
			temp.right = node(ele)
		return root
		
	def inorder(self,root):
		if root == None:
			return 
		self.inorder(root.left)
		print(root.data)
		self.inorder(root.right)

root = None
keys = [15, 10, 20, 8, 12, 16, 25]
b = BST() 
for key in keys:
    root = b.buildBST(root, key)
 
b.inorder(root)													