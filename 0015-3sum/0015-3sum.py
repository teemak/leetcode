class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def helper(nums, i, res):
            seen = set()
            j = i + 1
            while j < len(nums):
                diff = -nums[i] - nums[j]
                if diff in seen:
                    res.append([nums[i], nums[j], diff])
                    while j + 1 < len(nums) and nums[j] == nums[j + 1]:
                        j += 1
                seen.add(nums[j])
                j += 1

        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i - 1] != nums[i]:
                helper(nums, i, res)
        return res