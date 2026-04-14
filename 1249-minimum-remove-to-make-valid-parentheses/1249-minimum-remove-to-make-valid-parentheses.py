class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        result = []
        balance = 0

        for char in s:
            if char == '(':
                balance += 1
                result.append(char)
            elif char == ')':
                if balance > 0:
                    balance -= 1
                    result.append(char)
            else:
                result.append(char)

        final = []
        open_to_remove = balance

        for char in reversed(result):
            if char == '(' and open_to_remove > 0:
                open_to_remove -= 1
            else:
                final.append(char)
        
        return ''.join(reversed(final))
            