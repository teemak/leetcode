class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = defaultdict(list)
        p = prerequisites
        unvisited, visiting, visited = 0, 1, 2
        states = [unvisited] * numCourses

        for a, b in p:
            g[a].append(b)

        def dfs(node):
            state = states[node]
            if state == visited:
                return True
            if state == visiting:
                return False

            states[node] = visiting

            for n in g[node]:
                if not dfs(n):
                    return False

            states[node] = visited
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True