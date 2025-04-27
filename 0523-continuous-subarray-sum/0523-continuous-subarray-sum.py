class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainders = {0: -1}
        total = 0

        for i, num in enumerate(nums):
            total += num
            r = total % k
            if r not in remainders:
                remainders[r] = i
            elif i - remainders[r] > 1:
                return True
        return False