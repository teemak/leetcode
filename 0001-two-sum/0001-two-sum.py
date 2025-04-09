class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffs = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in diffs:
                return [i, diffs[diff]]
            diffs[nums[i]] = i
        
        return []
