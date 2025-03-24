class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = {}
        states = [0] * numCourses
        result = []

        for a, b in prerequisites:
            if a not in adj_list:
                adj_list[a] = []
            adj_list[a].append(b)

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
            result.append(node)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return result