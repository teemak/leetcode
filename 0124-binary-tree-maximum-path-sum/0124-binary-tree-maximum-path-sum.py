# Definition for a binary tree node.
# explanation: https://leetcode.com/problems/binary-tree-maximum-path-sum/solutions/603423/python-recursion-stack-thinking-process-diagram
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf')
        self.dfs(root)
        return self.max_sum

    def dfs(self, node):
        if not node:
            return 0

        left = max(self.dfs(node.left), 0)
        right = max(self.dfs(node.right), 0)

        current_sum = node.val + left + right
        self.max_sum = max(self.max_sum, current_sum)

        return node.val + max(left, right)
