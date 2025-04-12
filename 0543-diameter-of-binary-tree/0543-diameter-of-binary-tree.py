# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return (0, 0)

            left_h, left_d = dfs(node.left)
            right_h, right_d = dfs(node.right)
            curr_height = max(left_h, right_h) + 1
            diameter = left_h + right_h
            max_d = max(diameter, left_d, right_d)

            return (curr_height, max_d)
            
        return dfs(root)[1]


