class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        res = num = diff = 0

        for k in range(len(nums)):
            res = max(res, diff * nums[k])
            # update the best difference
            diff = max(diff, num - nums[k])
            # track the largest value seen
            num = max(num, nums[k])
        
        return res