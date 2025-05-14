class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        mod = 10**9+7

        def helper():
            t_mat = [[0] * 26 for _ in range(26)]
            for i in range(26):
                for j in range(1, nums[i] + 1):
                    t_mat[i][(i + j) % 26] += 1
            return t_mat

        def mat_mult(a, b):
            size = len(a)
            result = [[0] * size for _ in range(size)]
            for i in range(size):
                for j in range(size):
                    for k in range(size):
                        result[i][j] = (result[i][j] + a[i][k] * b[k][j]) % mod
            return result

        def mat_pow(mat, power):
            size = len(mat)
            result = [[1 if i == j else 0 for j in range(size)] for i in range(size)]

            while power:
                if power % 2 == 1:
                    result = mat_mult(result, mat)
                mat = mat_mult(mat, mat)
                power //= 2
            return result

        def vector_mul(vec, mat):
            result = [0] * 26
            for i in range(26):
                for j in range(26):
                    result[j] = (result[j] + vec[i] * mat[i][j]) % mod
            return result
        
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        T = helper()
        t_exp = mat_pow(T, t)
        final_freq = vector_mul(freq, t_exp)

        return sum(final_freq) % mod