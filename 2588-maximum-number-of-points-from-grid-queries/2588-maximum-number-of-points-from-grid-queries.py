from queue import PriorityQueue

class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        query_count = len(queries)
        result = [0] * query_count
        row_count = len(grid)
        col_count = len(grid[0])
        total_cells = row_count * col_count
        threshold = [0] * (total_cells + 1)
        min_val = [[float('inf')] * col_count for _ in range(row_count)]
        min_val[0][0] = grid[0][0]

        min_heap = PriorityQueue()
        min_heap.put((grid[0][0], 0, 0))
        visited_cells = 0

        while not min_heap.empty():
            current = min_heap.get()
        
            threshold[visited_cells + 1] = current[0]
            visited_cells += 1
            for direction in ([(1,0),(-1,0),(0,1),(0,-1)]):
                x, y = (current[1] + direction[0], current[2] + direction[1])
                if (0 <= x < row_count and 0 <= y < col_count and min_val[x][y] == float('inf')):
                    min_val[x][y] = max(current[0], grid[x][y])
                    min_heap.put((min_val[x][y], x, y))

        for i in range(query_count):
            target = queries[i] 
            left, right = 0, total_cells

            while left < right:
                mid = left + (right - left + 1) // 2
                if threshold[mid] < target:
                    left = mid
                else:
                    right = mid - 1

            result[i] = left
            
        return result