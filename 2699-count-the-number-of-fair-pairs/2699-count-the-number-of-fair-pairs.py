class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        count = 0
        n = len(nums)

        for i in range(n):
            lo = lower - nums[i]
            hi = upper - nums[i]

            left = bisect_left(nums, lo, i + 1)
            right = bisect_right(nums, hi, i + 1)

            count += right - left
            
        return count

