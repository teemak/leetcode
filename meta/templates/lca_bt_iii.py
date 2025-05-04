class Node:
    def __init__(self, val=0, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        pass  # Implement the logic here

# Build tree with parent pointers
def build_tree_with_parents():
    nodes = {val: Node(val) for val in [3, 5, 1, 6, 2, 0, 8, 7, 4]}
    root = nodes[3]

    root.left = nodes[5]; nodes[5].parent = root
    root.right = nodes[1]; nodes[1].parent = root
    nodes[5].left = nodes[6]; nodes[6].parent = nodes[5]
    nodes[5].right = nodes[2]; nodes[2].parent = nodes[5]
    nodes[1].left = nodes[0]; nodes[0].parent = nodes[1]
    nodes[1].right = nodes[8]; nodes[8].parent = nodes[1]
    nodes[2].left = nodes[7]; nodes[7].parent = nodes[2]
    nodes[2].right = nodes[4]; nodes[4].parent = nodes[2]

    return nodes

sol = Solution()
nodes = build_tree_with_parents()

# Test Case 1
print(sol.lowestCommonAncestor(nodes[5], nodes[1]).val)  # Output: 3

# Test Case 2
print(sol.lowestCommonAncestor(nodes[5], nodes[4]).val)  # Output: 5

# Test Case 3
print(sol.lowestCommonAncestor(nodes[1], nodes[2]).val)  # Output: 3

