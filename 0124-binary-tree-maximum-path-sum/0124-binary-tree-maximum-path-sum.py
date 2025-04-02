# Definition for a binary tree node.
# explanation: https://leetcode.com/problems/binary-tree-maximum-path-sum/solutions/603423/python-recursion-stack-thinking-process-diagram
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path = float('-inf')
        def helper(node):
            nonlocal max_path
            if node is None:
                return 0

            left = max(helper(node.left), 0)
            right = max(helper(node.right), 0)

            path = node.val + left + right
            max_path = max(max_path, path)

            return node.val + max(left, right)
        helper(root)
        return max_path