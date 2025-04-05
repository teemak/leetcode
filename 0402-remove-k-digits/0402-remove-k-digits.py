class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        for digit in num:
            while k > 0 and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)

        final = stack[:-k] if k else stack
        res = ''.join(final).lstrip('0')
        return res if res else '0'