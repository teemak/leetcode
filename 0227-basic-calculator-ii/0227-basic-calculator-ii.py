class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(' ', '')
        n = len(s)
        result = tail = num = i = 0
        operator = '+'

        while i < n:
            ch = s[i]

            if ch.isdigit():
                num = 0
                while i < n and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                if operator == '+':
                    result += num
                    tail = num
                elif operator == '-':
                    result -= num
                    tail = -num
                elif operator == '*':
                    result = result - tail + (tail * num)
                    tail = tail * num
                elif operator == '/':
                    result = result - tail + int(tail / num)
                    tail = int(tail / num)
                continue
            elif ch in '+-*/':
                operator = ch
            
            i += 1
        return result
                
