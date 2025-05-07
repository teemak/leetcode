class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        island_id = 2
        island_area = {}

        def dfs(r, c, id):
            if r < 0 or r >= n or c < 0 or c >= n or grid[r][c] != 1:
                return 0
            grid[r][c] = id
            area = 1
            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                area += dfs(r + dr, c + dc, id)
            return area
        
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    area = dfs(r, c, island_id)
                    island_area[island_id] = area
                    island_id += 1

        max_area = max(island_area.values(), default = 0)
        
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:
                    seen = set()
                    for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] > 1:
                            seen.add(grid[nr][nc])
                    area = sum(island_area[i] for i in seen) + 1
                    max_area = max(max_area, area)

        return max_area if max_area > 0 else n * n