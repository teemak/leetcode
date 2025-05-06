class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = []
        left = right = 0
        result = 0 

        while right < len(s):
            if s[right] not in window:
                window.append(s[right])
                right += 1
                result = max(result, len(window))
            else:
                window.pop(0)
                left += 1

        return result