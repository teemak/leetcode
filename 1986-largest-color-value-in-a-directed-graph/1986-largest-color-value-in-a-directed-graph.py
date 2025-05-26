from collections import defaultdict
from typing import List

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)

        visited = [0] * n  # 0 = unvisited, 1 = visiting, 2 = visited
        color_count = [[0] * 26 for _ in range(n)]
        self.has_cycle = False

        def dfs(node):
            if visited[node] == 1:
                self.has_cycle = True
                return
            if visited[node] == 2:
                return

            visited[node] = 1
            for neighbor in graph[node]:
                dfs(neighbor)
                for i in range(26):
                    color_count[node][i] = max(color_count[node][i], color_count[neighbor][i])

            color_index = ord(colors[node]) - ord('a')
            color_count[node][color_index] += 1
            visited[node] = 2

        for v in range(n):
            if visited[v] == 0:
                dfs(v)

        if self.has_cycle:
            return -1

        return max(max(counts) for counts in color_count)