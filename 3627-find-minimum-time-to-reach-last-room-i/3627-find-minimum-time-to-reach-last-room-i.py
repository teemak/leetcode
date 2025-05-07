import heapq

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n, m = len(moveTime), len(moveTime[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        time = [[float('inf')] * m for _ in range(n)]
        time[0][0] = 0
        heap = [(0, 0, 0)]

        while heap:
            curr_time, i, j = heapq.heappop(heap)

            if i == n - 1 and j == m - 1:
                return curr_time

            for dx, dy in directions:
                r, c = i + dx, j + dy

                if 0 <= r < n and 0 <= c < m:
                    next_time = max(curr_time, moveTime[r][c]) + 1

                    if next_time < time[r][c]:
                        time[r][c] = next_time
                        heapq.heappush(heap, (next_time, r, c))

        return -1 
        