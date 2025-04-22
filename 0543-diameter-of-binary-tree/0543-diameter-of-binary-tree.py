# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        stack = [(root, False)]
        depths = {} # depth of each node
        max_diameter = 0

        while stack:
            node, visited = stack.pop() 

            if node is None:
                continue

            if visited:
                left_depth = depths.get(node.left, 0)
                right_depth = depths.get(node.right, 0)

                max_diameter = max(max_diameter, left_depth + right_depth)
                depths[node] = max(left_depth, right_depth) + 1
            else:
                # post order
                stack.append((node, True))
                stack.append((node.right, False))
                stack.append((node.left, False))

        return max_diameter