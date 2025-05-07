class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []
        m, n = len(mat), len(mat[0])
        result = []
        diagonals = {}

        for i in range(m):
            for j in range(n):
                diag = i + j
                if diag not in diagonals:
                    diagonals[diag] = []
                diagonals[diag].append(mat[i][j])

        for diag in range(m + n - 1):
            if diag % 2 == 0:
                result.extend(reversed(diagonals[diag]))
            else:
                result.extend(diagonals[diag])

        return result