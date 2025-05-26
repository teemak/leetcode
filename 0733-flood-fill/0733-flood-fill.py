class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
        rows, cols = len(image), len(image[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        original = image[sr][sc]

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or image[r][c] != original:
                return 
            image[r][c] = color
            for dx, dy in directions:
                dfs(dx + r,  dy + c)
        dfs(sr, sc)
        return image