class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int, {0:1})
        curr = count = 0

        for num in nums:
            curr += num
            count += freq[curr - k]
            freq[curr] += 1

        return count
