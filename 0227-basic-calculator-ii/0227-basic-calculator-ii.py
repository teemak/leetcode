class Solution:
    def calculate(self, s: str) -> int:
        i = cur = prev = res = 0
        operator = '+'

        while i < len(s):
            element = s[i]
            if element.isdigit():
                while i < len(s) and s[i].isdigit():
                    cur = cur * 10 + int(s[i])
                    i += 1
                i -= 1
                if operator == '+':
                    res += cur
                    prev = cur
                elif operator == '-':
                    res -= cur
                    prev = -cur
                elif operator == '*':
                    res -= prev
                    res += prev * cur
                    prev = cur * prev
                else:
                    res -= prev
                    res += int(prev/cur)
                    prev = int(prev/cur)
                cur = 0
            elif element != ' ':
                operator = element
            i += 1
        return res

