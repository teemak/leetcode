class Solution:
    def calculate(self, s: str) -> int:
        def helper(s, i):
            num = 0
            stack = []
            sign = '+'

            while i < len(s):
                ch = s[i]
                if ch.isdigit():
                    num = num * 10 + int(ch)

                if ch in '+-*/' or i == len(s) - 1:
                    if sign == '+':
                        stack.append(num)
                    elif sign == '-':
                        stack.append(-num)
                    elif sign == '*':
                        stack[-1] *= num
                    elif sign == '/':
                        stack[-1] = int(stack[-1] / num)
                    sign = ch
                    num = 0
                i += 1
            return sum(stack)
        return helper(s.replace(' ', ''), 0)