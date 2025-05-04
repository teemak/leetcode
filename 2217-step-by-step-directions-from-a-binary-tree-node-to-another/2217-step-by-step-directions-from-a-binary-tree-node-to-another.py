# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def findLCA(node):
            if not node or node.val == startValue or node.val == destValue:
                return node
            left = findLCA(node.left)
            right = findLCA(node.right)
            if left and right:
                return node
            return left if left else right

        def getPath(node, target, path):
            if not node:
                return False
            if node.val == target:
                return True
            path.append('L')
            if getPath(node.left, target, path):
                return True
            path.pop()
            path.append('R')
            if getPath(node.right, target, path):
                return True
            path.pop()
            return False

        lca = findLCA(root)
        pathToStart, pathToDest = [], []
        getPath(lca, startValue, pathToStart)
        getPath(lca, destValue, pathToDest)

        return 'U' * len(pathToStart) + ''.join(pathToDest)
