mod = 10**9 + 7

class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        max_length = 15
        max_comb = n + 10
        fact = [1] * max_comb
        inv = [1] * max_comb

        for i in range(1, max_comb):
            fact[i] = fact[i - 1] * i % mod
        
        inv[-1] = pow(fact[-1], mod - 2, mod)
        
        for i in range(max_comb - 2, -1, -1):
            inv[i] = inv[i + 1] * (i + 1) % mod

        def compute(n, k):
            if k < 0 or k > n:
                return 0
            return fact[n] * inv[k] % mod * inv[n - k] % mod
        
        dp = [0] * (maxValue + 1)
        res = 0

        seq_by_val = [defaultdict(int) for _ in range(maxValue + 1)]

        for val in range(1, maxValue + 1):
            seq_by_val[val][1] = 1

        for length in range(2, max_length + 1):
            for val in range(1, maxValue + 1):
                for div in range(val * 2, maxValue + 1, val):
                    seq_by_val[div][length] += seq_by_val[val][length - 1]

        for val in range(1, maxValue + 1):
            for length, count in seq_by_val[val].items():
                res += count * compute(n - 1, length - 1)
                res %= mod

        return res


