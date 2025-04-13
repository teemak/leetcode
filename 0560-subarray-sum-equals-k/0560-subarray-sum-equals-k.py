class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count, curr_sum = 0, 0
        prefix_sums = defaultdict(int)
        prefix_sums[0] = 1

        for num in nums:
            curr_sum += num
            count += prefix_sums[curr_sum - k]
            prefix_sums[curr_sum] += 1

        return count