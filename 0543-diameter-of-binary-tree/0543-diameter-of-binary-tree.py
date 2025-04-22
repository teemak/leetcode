# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
         1
       /  \
      2    3
     / \
    4   5

'''
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        
        def dfs(node):
            nonlocal diameter
            
            if not node:
                return 0
                
            left = dfs(node.left) #4 - 0, #2
            right = dfs(node.right)  #5 - 0
            diameter = max(diameter, left + right) #2 - 2 3 - 0, 1 2, 1:3
            return max(left, right) + 1
            
        dfs(root)
        return diameter
        