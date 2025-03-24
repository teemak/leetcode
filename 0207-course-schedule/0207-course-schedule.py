class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = {}
        states = [0] * numCourses

        for a, b in prerequisites:
            if b not in adj_list:
                adj_list[b] = []
            adj_list[b].append(a)

        def dfs(node):
            if states[node] == 1:
                return False
            if states[node] == 2:
                return True

            states[node] = 1
            if node in adj_list:
                for n in adj_list[node]:
                    if not dfs(n):
                        return False

            states[node] = 2
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True