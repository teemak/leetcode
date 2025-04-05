class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])
        prefix = [[0] * (n + 1) for _ in range(m + 1)]
        lo, hi = 0, min(m, n)
        res = 0

        for i in range(m):
            for j in range(n):
                prefix[i+1][j+1] = mat[i][j] + prefix[i][j+1] + prefix[i+1][j] - prefix[i][j]

        def condition(k):
            for i in range(k, m + 1):
                for j in range(k, n + 1):
                    total = prefix[i][j] - prefix[i-k][j] - prefix[i][j-k] + prefix[i-k][j-k]
                    if total <= threshold:
                        return True
            return False

        while lo <= hi:
            mid = (hi + lo) // 2
            if condition(mid):
                res = mid
                lo = mid + 1
            else:
                hi = mid - 1

        return res