class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, current_sum = 0, 0
        result = float('inf')

        for right in range(len(nums)):
            current_sum += nums[right]

            while current_sum >= target:
                result = min(result, right - left + 1)
                current_sum -= nums[left]
                left += 1

        result = result if result != float('inf') else 0
        return result