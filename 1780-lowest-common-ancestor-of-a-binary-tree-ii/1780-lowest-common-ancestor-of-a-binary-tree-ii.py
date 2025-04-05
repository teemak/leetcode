# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node):
            if not node:
                return False, False, None

            left_p, left_q, left_lca = dfs(node.left)
            right_p, right_q, right_lca = dfs(node.right)

            found_p = left_p or right_p or node == p
            found_q = left_q or right_q or node == q

            if left_lca:
                return found_p, found_q, left_lca
            if right_lca:
                return found_p, found_q, right_lca
            if found_p and found_q:
                return True, True, node

            return found_p, found_q, None

        found_p, found_q, lca = dfs(root)
        return lca if found_p and found_q else None
