class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        moves = 0
        prev = -1

        for num in nums:
            if num <= prev:
                moves += prev + 1 - num
                prev += 1
            else:
                prev = num
        return moves