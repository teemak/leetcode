import heapq

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n, m = len(moveTime), len(moveTime[0])
        time = [[float('inf')] * m for _ in range(n)]
        pq = []
        heapq.heappush(pq, (0, 0, 0))
        time[0][0] = 0

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while pq:
            t, i, j = heapq.heappop(pq)

            if i == n - 1 and j == m - 1:
                return t

            for dx, dy in directions:
                r, s = i + dx, j + dy
                if r < 0 or r >= n or s < 0 or s >= m:
                    continue

                next_time = max(t, moveTime[r][s]) + 1
                if next_time < time[r][s]:
                    time[r][s] = next_time
                    heapq.heappush(pq, (next_time, r, s))
        return -1 
        