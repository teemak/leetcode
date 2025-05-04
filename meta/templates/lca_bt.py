# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        pass  # Implement logic here


# Helper to insert children manually for LCA tree testing
def build_sample_tree():
    # Tree: [3,5,1,6,2,0,8,null,null,7,4]
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)
    return root

sol = Solution()

# Test Case 1
tree = build_sample_tree()
p1 = tree.left               # Node 5
q1 = tree.right              # Node 1
print(sol.lowestCommonAncestor(tree, p1, q1).val)  # Output: 3

# Test Case 2
p2 = tree.left               # Node 5
q2 = tree.left.right.right  # Node 4
print(sol.lowestCommonAncestor(tree, p2, q2).val)  # Output: 5

# Test Case 3
tree2 = TreeNode(1)
tree2.left = TreeNode(2)
p3 = tree2                   # Node 1
q3 = tree2.left              # Node 2
print(sol.lowestCommonAncestor(tree2, p3, q3).val)  # Output: 1

