class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        left, longest = 0, 0

        for char in s:
            while char in window:
                window.remove(s[left])
                left += 1
            window.add(char)
            longest = max(longest, len(window))
        
        return longest
        