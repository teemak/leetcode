class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        left = 0

        for i, num in enumerate(nums):
            if left == (total_sum - left - num):
                return i
            left += num

        return -1

