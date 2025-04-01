class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        total_buildings = sum(row.count(1) for row in grid)

        distance = [[0] * cols for _ in range(rows)]
        reachable = [[0] * cols for _ in range(rows)]
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        def bfs(x, y):
            visited = [[False] * cols for _ in range(rows)]
            queue = deque([(x, y, 0)])
            visited[x][y] = True
            num_reached = 0

            while queue:
                x1, y1, dist = queue.popleft()

                for dx, dy in directions:
                    nx, ny = dx + x1, dy + y1
                    if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny] and grid[nx][ny] == 0:
                        visited[nx][ny] = True
                        distance[nx][ny] += dist + 1
                        reachable[nx][ny] += 1
                        queue.append((nx, ny, dist + 1))
                        num_reached += 1

            return num_reached

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    if bfs(row, col) == 0:
                        return -1
        
        min_distance = float('inf')
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0 and reachable[row][col] == total_buildings:
                    min_distance = min(min_distance, distance[row][col])
        
        return min_distance if min_distance != float('inf') else -1