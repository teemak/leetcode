class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        unique_pals = set()
        base = 10 ** ((n - 1) // 2)
        skip = n & 1

        for i in range(base, base * 10):
            s = str(i)
            s += s[::-1][skip:]
            pal_int = int(s)
            if pal_int % k == 0:
                sorted_s = ''.join(sorted(s))
                unique_pals.add(sorted_s)

        fact = [factorial(i) for i in range(n + 1)]
        ans = 0

        for s in unique_pals:
            cnt = [0] * 10

            for c in s:
                cnt[int(c)] += 1

            total = 0

            for digit in range(1, 10):

                if cnt[digit] == 0:
                    continue

                cnt[digit] -= 1
                perms = fact[n - 1]

                for c in cnt:
                    perms //= fact[c]

                total += perms
                cnt[digit] += 1
            ans += total
        return ans