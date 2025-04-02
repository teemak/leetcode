class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not word:
            return False

        rows, cols = len(board), len(board[0])
        n = len(word)
        if n > rows * cols:
            return False
        cell_counts = Counter(cell for row in board for cell in row)
        char_counts = Counter(word)
        for char, count in char_counts.items():
            if cell_counts[char] < count:
                return False
        
        if char_counts[word[-1]] < char_counts[word[0]]:
            word = word[::-1]
        
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        def dfs(row, col, index, visited):
            if index == n:
                return True
            if row < 0 or row >= rows or col < 0 or col >= cols or (row, col) in visited or board[row][col] != word[index]:
                return False
            visited.add((row, col))
            for dx, dy in directions:
                x, y = dx + row, dy + col
                if dfs(x, y, index + 1, visited):
                    return True
            visited.remove((row, col))
            return False

        for row in range(rows):
            for col in range(cols):
                if dfs(row, col, 0, set()):
                    return True
        
        return False