class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        adj_list = defaultdict(list)
        for a, b in dislikes:
            adj_list[a].append(b)
            adj_list[b].append(a)

        color = [0] * (n + 1)

        def dfs(node, c):
            if color[node] != 0:
                return color[node] == c
            color[node] = c
        
            for n in adj_list[node]:
                if not dfs(n, -c):
                    return False
            return True

        for i in range(1, n + 1):
            if color[i] == 0 and not dfs(i, 1):
                return False
        return True