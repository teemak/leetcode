class Solution:
    def calculate(self, s: str) -> int:
        def precedence(op):
            if op in '*/':
                return 2
            if op in '+-':
                return 1
            return 0
        def apply_op(op, b, a):
            if op == '+': return a + b
            if op == '-': return a - b
            if op == '*': return a * b
            if op == '/': return int(a // b)
        nums = []
        ops = []
        i = 0
        n = len(s)

        while i < n:
            if s[i] == ' ':
                i += 1
                continue
            if s[i].isdigit():
                num = 0
                while i < n and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                nums.append(num)
            else:
                while ops and precedence(ops[-1]) >= precedence(s[i]):
                    op = ops.pop()
                    b = nums.pop()
                    a = nums.pop()
                    nums.append(apply_op(op, b, a))
                ops.append(s[i])
                i += 1
        while ops:
            op = ops.pop()
            b = nums.pop()
            a = nums.pop()
            nums.append(apply_op(op, b, a))
        return nums[0] 