class node:
	def __init__(self,ele):
		self.info = ele
		self.right = None
		self.left = None

class BST:
	def buildBST(self,root_node,ele):
		if root_node is None:
			return node(ele)	
		if ele < root_node.info:
			root_node.left = self.buildBST(root_node.left,ele)
		elif ele > root_node.info:
			root_node.right = self.buildBST(root_node.right,ele)
		return root_node
		
	def countNodes(self,root_node):
		if root_node is None:
			return 0
		return 1 + self.countNodes(root_node.left) + self.countNodes(root_node.right)

	def countLeafs(self,root_node):
		if (root_node is None):
			return 0
		if (root_node.left is None and root_node.right is None):	
			return 1
		else:
			return self.countNodes(root_node.left) + self.countNodes(root_node.right)

	def max_depth(self,root_node):
		if root_node is None:
			return 0
		else:
			lh = self.max_depth(root_node.left)			
			rh = self.max_depth(root_node.right)	
			return max(lh,rh) + 1			
		
b = BST()
root = None
for i in [1,2,3,4,5,6,12,9,45,10,7,43,8,11]:
	root = b.buildBST(root,i)
t_nodes = b.countNodes(root)
t_leafs = b.countLeafs(root)
print(t_nodes,t_leafs)