class Solution:
    def romanToInt(self, s: str) -> int:
        numerals = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        total = numerals.get(s[-1])

        for i in reversed(range(len(s) - 1)):
            if numerals[s[i]] < numerals[s[i + 1]]:
                total -= numerals[s[i]]
            else:
                total += numerals[s[i]]
        return total
