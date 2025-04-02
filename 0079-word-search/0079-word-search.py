class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        def dfs(row, col, index):
            # happy case
            if index == len(word):
                return True
            # base case - out of bounds
            if row < 0 or row >= rows or col < 0 or col >= cols or board[row][col] != word[index]:
                return False
            # mark cell as visited
            temp, board[row][col] = board[row][col], '#'
            # recursive case
            for dx, dy in directions:
                x, y = dx + row, dy + col
                if dfs(x, y, index + 1):
                    return True
            # backtrack
            board[row][col] = temp

            return False

        for row in range(rows):
            for col in range(cols):
                if dfs(row, col, 0):
                    return True
        
        return False