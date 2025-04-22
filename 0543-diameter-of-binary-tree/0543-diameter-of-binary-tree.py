# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # keep traversing until at child node
        edges = 0
        def dfs(node):
            nonlocal edges
            if node is None:
                return 0
            # recurse up keeping a count of edges
            left = dfs(node.left)
            right = dfs(node.right)
            edges = max(edges, left + right)
            return 1 + max(left, right)

        dfs(root)
        return edges
            
