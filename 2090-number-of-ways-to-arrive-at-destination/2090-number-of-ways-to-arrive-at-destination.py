class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        mod = 10**9 + 7
        graph = {i: [] for i in range(n)}

        for u, v, time in roads:
            graph[u].append((v, time))
            graph[v].append((u, time))

        pq = [(0, 0)]
        dist = [float('inf')] * n
        ways = [0] * n
        dist[0] = 0
        ways[0] = 1 

        while pq:
            time, node = heapq.heappop(pq)
            if time > dist[node]:
                continue
            for neighbor, travel in graph[node]:
                new_time = time + travel

                if new_time < dist[neighbor]:
                    dist[neighbor] = new_time
                    ways[neighbor] = ways[node]
                    heapq.heappush(pq, (new_time, neighbor))
                elif new_time == dist[neighbor]:
                    ways[neighbor] = (ways[neighbor] + ways[node]) % mod
        return ways[n - 1]