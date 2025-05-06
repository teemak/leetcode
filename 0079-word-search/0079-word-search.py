class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        def dfs(r, c, i):
            #base case
            if i == len(word):
                return True
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[i]:
                return

            temp = board[r][c]
            board[r][c] = '#'

            #recursive case
            for dx, dy in directions:
                if dfs(r + dx, c + dy, i + 1):
                    return True

            board[r][c] = temp
            return False


        for row in range(rows):
            for col in range(cols):
                if dfs(row,col,0):
                    return True
        return False