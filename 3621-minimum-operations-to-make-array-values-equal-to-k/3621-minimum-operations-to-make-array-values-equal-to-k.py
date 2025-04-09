class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        if min(nums) < k:
            return -1
        return len(set(nums)) + (min(nums) > k) - 1