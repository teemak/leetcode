class Solution:
    def calculate(self, s: str) -> int:
        n = len(s)
        operator = '+'
        num = result = tail = i = 0

        while i < n:
            element = s[i]
            if element.isdigit():
                num = 0
                while i < n and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                match operator:
                    case '+':
                        result += num
                        tail = num
                    case '-':
                        result -= num
                        tail = -num
                    case '*':
                        result = result - tail + (tail * num)
                        tail = tail * num
                    case '/':
                        result = result - tail + int(tail / num)
                        tail = int(tail / num)
                num = 0
                continue
            elif element in '+-*/':
                operator = element
            i += 1
        return result