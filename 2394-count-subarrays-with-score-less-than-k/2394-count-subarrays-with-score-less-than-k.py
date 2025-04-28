class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        left = curr_sum = count = 0
        for right in range(len(nums)):
            curr_sum += nums[right]

            while left <= right and curr_sum * (right - left + 1) >= k:
                curr_sum -= nums[left]
                left += 1
            
            count += (right - left + 1)

        return count