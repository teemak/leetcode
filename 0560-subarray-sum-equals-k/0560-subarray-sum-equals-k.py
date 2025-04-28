class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sums = {0: 1}
        running_count = 0

        for i, num in enumerate(nums):
            running_count += num
            diff = running_count - k
            if diff in prefix_sums:
                count += prefix_sums[diff]
            prefix_sums[running_count] = prefix_sums.get(running_count, 0) + 1
        return count