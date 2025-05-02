class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefix_sums = [0]
        for i in range(len(nums)):
            prefix_sums.append(prefix_sums[i] + nums[i])
        return prefix_sums[1:]