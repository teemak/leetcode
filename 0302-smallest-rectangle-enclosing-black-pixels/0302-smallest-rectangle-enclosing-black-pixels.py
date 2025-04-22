class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        m, n = len(image), len(image[0])

        def blackCol(col):
            return any(image[i][col] == '1' for i in range(m))

        def blackRow(row):
            return any(image[row][j] == '1' for j in range(n))

        left, right = 0, y

        while left < right:
            mid = (left + right) // 2
            if blackCol(mid):
                right = mid
            else:
                left = mid + 1
        min_col = left

        left = y
        right = n - 1

        while left < right:
            mid = (left + right + 1) // 2
            if blackCol(mid):
                left = mid
            else:
                right = mid - 1
        
        max_col = left

        top, bot = 0, x
        while top < bot:
            mid = (top + bot) // 2
            if blackRow(mid):
                bot = mid
            else: 
                top = mid + 1
        min_row = top

        top, bot = x, m - 1

        while top < bot:
            mid = (top + bot + 1) // 2
            if blackRow(mid):
                top = mid
            else:
                bot = mid - 1
        max_row = top
        return (max_row - min_row + 1) * (max_col - min_col + 1)