class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        current_num = 0
        operator = '+'
        n = len(s)

        for i, ch in enumerate(s):
            if ch.isdigit():
                current_num = current_num * 10 + int(ch)
            
            if ch in '+-*/' or i == n - 1:
                if operator == '+':
                    stack.append(current_num)
                elif operator == '-':
                    stack.append(-current_num)
                elif operator == '*':
                    stack[-1] = stack[-1] * current_num
                elif operator == '/':
                    stack[-1] = int(stack[-1] / current_num)

                operator = ch
                current_num = 0

        return sum(stack) 