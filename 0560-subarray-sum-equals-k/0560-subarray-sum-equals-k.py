class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sum = 0
        prefix_map = defaultdict(int)
        prefix_map[0] = 1

        for num in nums:
            prefix_sum += num
            count += prefix_map[prefix_sum - k]
            prefix_map[prefix_sum] += 1

        return count