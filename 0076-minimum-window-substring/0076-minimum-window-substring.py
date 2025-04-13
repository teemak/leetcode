class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ''
        need = Counter(t)
        window = defaultdict(int)
        have = left = 0
        need_uniques = len(need)
        min_len = float('inf')
        res = ''

        for right, char in enumerate(s):
            window[char] += 1
            if char in need and window[char] == need[char]:
                have += 1
            while have == need_uniques:
                if (right - left + 1) < min_len:
                    min_len = right - left + 1
                    res = s[left:right + 1]
                window[s[left]] -= 1
                if s[left] in need and window[s[left]] < need[s[left]]:
                    have -= 1
                left += 1

        return res