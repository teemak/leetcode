class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh, rotten = set(), deque()
        rows, cols = len(grid), len(grid[0])

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    fresh.add((row, col))
                elif grid[row][col] == 2:
                    rotten.append((row, col))
        
        counter = 0
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        while fresh and rotten:
            counter += 1

            for _ in range(len(rotten)):
                row, col = rotten.popleft()

                for dx, dy in directions:
                    newx, newy = dx + row, dy + col
                    if (newx, newy) in fresh:
                        fresh.remove((newx, newy))
                        rotten.append((newx, newy))

        return -1 if fresh else counter