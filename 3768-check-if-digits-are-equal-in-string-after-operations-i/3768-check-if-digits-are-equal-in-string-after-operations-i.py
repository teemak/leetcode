class Solution:
    def hasSameDigits(self, s: str) -> bool:
        s = [int(d) for d in s]
        lt, rt = s[0], s[1]
        multiplier = 1

        for i in range(1, n:=len(s) - 1):
            multiplier = (multiplier*(n-i)) // i
            lt = (lt + s[i]*(multiplier % 10)) % 10
            rt = (rt + s[i + 1]*(multiplier % 10)) % 10
        return lt == rt