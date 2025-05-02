class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sum = 0
        prefix_map = defaultdict(int)
        prefix_map[0] = 1

        for num in nums:
            prefix_sum += num
            diff = prefix_sum - k
            count += prefix_map[diff]
            prefix_map[prefix_sum] += 1

        return count