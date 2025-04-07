"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node

        visited = {}
        queue = deque([node])
        visited[node] = Node(node.val, [])

        while queue:
            nay = queue.popleft()
            for n in nay.neighbors:
                if n not in visited:
                    visited[n] = Node(n.val, [])
                    queue.append(n)
                visited[nay].neighbors.append(visited[n])

        return visited[node]