class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(' ', '')
        n = len(s)
        num = 0
        last_op = '+'
        result = 0
        tail = 0
        i = 0

        while i < n:
            ch = s[i]
            if ch.isdigit():
                num = 0
                while i < n and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                i -= 1
            if not ch.isdigit() or i == n - 1:
                if last_op == '+':
                    result += num
                    tail = num
                elif last_op == '-':
                    result -= num
                    tail = -num
                elif last_op == '*':
                    result = result - tail + (tail * num)
                    tail = tail * num
                elif last_op == '/':
                    result = result - tail + int(tail / num)
                    tail = int(tail / num)
                last_op = ch
            i += 1
        return result