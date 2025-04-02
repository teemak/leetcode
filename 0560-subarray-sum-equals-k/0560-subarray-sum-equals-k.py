class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixes = defaultdict(int, {0:1})
        count = total = 0

        for num in nums:
            count += num
            diff = count - k
            total += prefixes[diff]
            prefixes[count] += 1

        return total
