class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def k_sum(nums, target, k):
            res = []
            if not nums:
                return res
            
            avg_val = target // k

            if avg_val < nums[0] or nums[-1] < avg_val:
                return res
            
            if k == 2:
                return two_sum(nums, target)
            
            for i in range(len(nums)):
                if i == 0 or nums[i - 1] != nums[i]:
                    for subset in k_sum(nums[i + 1:], target - nums[i], k - 1):
                        res.append([nums[i]] + subset)
            return res

        def two_sum(nums, target):
            res = []
            lo, hi = 0, len(nums) - 1

            while lo < hi:
                curr_sum = nums[lo] + nums[hi]
                if curr_sum < target or (lo > 0 and nums[lo] == nums[lo - 1]):
                    lo += 1
                elif curr_sum > target or (hi < len(nums) - 1 and nums[hi] == nums[hi + 1]):
                    hi -= 1
                else:
                    res.append([nums[lo], nums[hi]])
                    lo += 1
                    hi -= 1
            return res
        
        nums.sort()
        return k_sum(nums, target, 4)