class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        product = 1
        zero_count = 0

        for i, num in enumerate(nums):
            if num == 0:
                zero_count += 1
            else:
                product *= num
        
        result = []

        for i, num in enumerate(nums):
            if zero_count > 1:
                # handles multiple zeros
                result.append(0)
            elif zero_count == 1:
                # need to account for division by zero
                result.append(product if num == 0 else 0)
            else :
                result.append(product // num)

        return result
