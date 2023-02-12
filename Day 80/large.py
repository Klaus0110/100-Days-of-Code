class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

def kthLargest(root: TreeNode, k: int) -> int:
	st = []
	curr = root
	count = 0
	while curr or st:
		while curr:
			st.append(curr)
			curr = curr.right
		curr = st.pop()
		count += 1
		if count == k:
			return curr.val
		curr = curr.left
	return -1

# create a BST
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(7)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.left = TreeNode(6)
root.right.right = TreeNode(8)

# find the kth largest element
k = 3
kth_largest = kthLargest(root, k)
if kth_largest != -1:
	print(f"The {k}th largest element is: {kth_largest}")
else:
	print(f"The {k}th largest element does not exist")
