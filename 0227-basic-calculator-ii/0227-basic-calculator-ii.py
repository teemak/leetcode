class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(' ', '')
        n = len(s)
        result = tail = num = i = 0
        op = '+'

        while i < n:
            ch = s[i]
            if '0' <= ch <= '9':
                num = 0
                while i < n and '0' <= s[i] <= '9':
                    num = num * 10 + ord(s[i]) - ord('0')
                    i += 1

                if op == '+':
                    result += num
                    tail = num
                elif op == '-':
                    result -= num
                    tail = -num
                elif op == '*':
                    result = result - tail + (tail * num)
                    tail = tail * num
                elif op == '/':
                    result = result - tail + int(tail / num)
                    tail = int(tail / num)
                continue
            else:
                op = ch
            i += 1
        return result

