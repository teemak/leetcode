class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        sum_to_idx = {}
        prefix_sum, max_len = 0, 0
        for i, num in enumerate(nums):
            prefix_sum += num

            if prefix_sum == k:
                max_len = i + 1

            diff = prefix_sum - k 
            if diff in sum_to_idx:
                max_len = max(max_len, i - sum_to_idx[diff])
            
            if prefix_sum not in sum_to_idx:
                sum_to_idx[prefix_sum] = i

        return max_len