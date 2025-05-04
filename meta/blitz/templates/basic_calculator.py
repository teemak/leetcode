class Solution:
    def calculate(self, s: str) -> int:
        pass


# Test Case 1
s = "3+2*2"
# Output: 7
# Explanation: Multiplication happens before addition → 3 + (2 * 2) = 7

# Test Case 2
s = " 3/2 "
# Output: 1
# Explanation: Integer division truncates toward zero → 3 // 2 = 1

# Test Case 3
s = " 3+5 / 2 "
# Output: 5
# Explanation: 5 / 2 = 2 (integer division), then 3 + 2 = 5

# Test Case 4
s = "14-3/2"
# Output: 13
# Explanation: 3 / 2 = 1 → 14 - 1 = 13

# Test Case 5
s = "0-2147483647"
# Output: -2147483647

# Test Case 6
s = "100*2+12"
# Output: 212

# Test Case 7
s = " 10 + 2 * 6 "
# Output: 22

# Test Case 8
s = " 100 * 2 + 12 "
# Output: 212

# Test Case 9
s = " 100 * ( 2 + 12 ) "  # Not valid as per the problem description, parentheses aren't supported

# Test Case 10
s = "3+5 / 2 * 2"
# Output: 7
# Explanation: 5 / 2 = 2 → 2 * 2 = 4 → 3 + 4 = 7

