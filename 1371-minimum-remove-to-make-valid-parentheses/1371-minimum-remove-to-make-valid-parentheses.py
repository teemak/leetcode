class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        idx_remove = set()
        stack = []

        for i, char in enumerate(s):
            if char not in '()':
                continue
            if char == '(':
                stack.append(i)
            elif not stack:
                idx_remove.add(i)
            else:
                stack.pop()

        idx_remove = idx_remove.union(set(stack))
        res = [] 
        for i, char in enumerate(s):
            if i not in idx_remove:
                res.append(char)
        return ''.join(res)
            
