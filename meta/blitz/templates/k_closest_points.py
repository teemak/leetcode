from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pass


# Test Case 1: Example from the problem
points = [[1,3], [-2,2]]
k = 1
# Closest point is [-2,2] with distance sqrt(4 + 4) = sqrt(8)
# Expected Output: [[-2,2]]

# Test Case 2: Two closest out of four
points = [[3,3], [5,-1], [-2,4], [0,0]]
k = 2
# Expected Output: [[0,0], [3,3]] or [[3,3], [0,0]] – order doesn't matter

# Test Case 3: k equals number of points
points = [[2,2], [1,1], [-1,-1]]
k = 3
# All points returned
# Expected Output: [[2,2], [1,1], [-1,-1]] in any order

# Test Case 4: Multiple points at same distance
points = [[1,1], [-1,-1], [1,-1], [-1,1]]
k = 2
# All have distance sqrt(2), any two should be returned
# Expected Output: any two from the list

# Test Case 5: Single point
points = [[100, -100]]
k = 1
# Expected Output: [[100, -100]]

