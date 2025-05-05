# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        self.root_nodes = []    
        def dfs(node):
            if node.left and not node.right:
                self.root_nodes.append(node.left.val)
            if node.right and not node.left:
                self.root_nodes.append(node.right.val)
            
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
                
        dfs(root)
        return self.root_nodes
            
    