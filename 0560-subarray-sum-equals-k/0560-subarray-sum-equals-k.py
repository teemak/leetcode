class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = defaultdict(int, {0:1})
        current_sum = subarrays = 0

        for num in nums:
            current_sum += num
            diff = current_sum - k
            subarrays += prefix_sum[diff]
            prefix_sum[current_sum] += 1

        return subarrays
