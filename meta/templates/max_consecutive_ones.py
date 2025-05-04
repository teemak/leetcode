from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        pass

# Test Case 1
nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
# Expected Output: 6
# Explanation: Flip the two zeros at indices 4 and 5 → [1,1,1,0,0,1,1,1,1,1,1]

# Test Case 2
nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k = 3
# Expected Output: 10

# Test Case 3
nums = [1,1,1,1,1]
k = 0
# Expected Output: 5
# Already all ones, no need to flip

# Test Case 4
nums = [0,0,0,0]
k = 4
# Expected Output: 4
# All zeros can be flipped

# Test Case 5
nums = [0,1,0,1,0,1,0,1,0,1]
k = 2
# Expected Output: 5
# Best window after flipping two 0's: [1,0,1,0,1,0,1] → flip two zeros to get five consecutive 1s

# Test Case 6
nums = [1,0,1,0,1]
k = 1
# Expected Output: 3

# Test Case 7
nums = [1]
k = 0
# Expected Output: 1

# Test Case 8
nums = [0]
k = 0
# Expected Output: 0

# Test Case 9
nums = [0]
k = 1
# Expected Output: 1

# Test Case 10
nums = [1,1,0,0,1,1,1,0,0,1]
k = 2
# Expected Output: 7

