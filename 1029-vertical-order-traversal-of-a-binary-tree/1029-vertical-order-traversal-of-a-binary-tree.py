# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque([(root, 0, 0)])
        col_table = defaultdict(list)

        while queue:
            node, row, col = queue.popleft()
            if node:
                col_table[col].append((row, node.val))
                queue.append((node.left, row + 1, col - 1))
                queue.append((node.right, row + 1, col + 1))

        sorted_cols = sorted(col_table.items())
        result = []
        for col, nodes in sorted_cols:
            nodes.sort(key = lambda x: (x[0], x[1]))
            result.append([val for row, val in nodes])

        return result
