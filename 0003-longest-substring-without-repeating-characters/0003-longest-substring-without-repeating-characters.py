class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = []
        longest = 0

        for char in s:
            while char in window:
                window.pop(0)
            window.append(char)
            longest = max(longest, len(window))

        return longest