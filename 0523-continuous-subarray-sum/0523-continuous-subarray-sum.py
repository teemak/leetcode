class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainders = {0: -1}
        total = 0

        for i, num in enumerate(nums):
            total += num
            remainder = total % k

            if remainder in remainders:
                if i - remainders[remainder] > 1:
                    return True
            else:
                remainders[remainder] = i

        return False
            