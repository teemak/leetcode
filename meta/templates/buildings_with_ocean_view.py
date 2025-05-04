# 1726 https://leetcode.com/problems/buildings-with-an-ocean-view/
from typing import List

class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        pass  # Implement the logic here

sol = Solution()

# Test Case 1
print(sol.findBuildings([4, 2, 3, 1]))  # Output: [0, 2, 3]

# Test Case 2
print(sol.findBuildings([4, 3, 2, 1]))  # Output: [0, 1, 2, 3]

# Test Case 3
print(sol.findBuildings([1, 3, 2, 4]))  # Output: [3]

# Edge Case 1: Only one building
print(sol.findBuildings([10]))  # Output: [0]

# Edge Case 2: All buildings same height
print(sol.findBuildings([2, 2, 2, 2]))  # Output: [3]

