class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int, {0:1})
        prefix = count = 0

        for num in nums:
            prefix += num
            count += freq[prefix - k]
            freq[prefix] += 1

        return count
