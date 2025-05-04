# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        pass  # You would implement the logic here

# Helper function to insert nodes into a BST
def insert_into_bst(root, val):
    if not root:
        return TreeNode(val)
    if val < root.val:
        root.left = insert_into_bst(root.left, val)
    else:
        root.right = insert_into_bst(root.right, val)
    return root

# Helper function to build a BST from list input
def build_bst(values):
    root = None
    for val in values:
        if val is not None:
            root = insert_into_bst(root, val)
    return root

# Build the BST and run tests
sol = Solution()

# Test Case 1
root1 = build_bst([6,2,8,0,4,7,9,3,5])
p1 = TreeNode(2)
q1 = TreeNode(8)
print(sol.lowestCommonAncestor(root1, p1, q1).val)  # Expected: 6

# Test Case 2
p2 = TreeNode(2)
q2 = TreeNode(4)
print(sol.lowestCommonAncestor(root1, p2, q2).val)  # Expected: 2

# Test Case 3
root3 = build_bst([2,1])
p3 = TreeNode(2)
q3 = TreeNode(1)
print(sol.lowestCommonAncestor(root3, p3, q3).val)  # Expected: 2

