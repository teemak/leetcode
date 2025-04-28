class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prefix_sums = [0]
        for i in range(len(nums)):
            self.prefix_sums.append(self.prefix_sums[i] + self.nums[i])

    def sumRange(self, left: int, right: int) -> int:
        # if left == right:
        #     return self.nums[left]
        # if len(self.nums) == 1 or left == 0:
        #     return self.nums[right]
        return self.prefix_sums[right + 1] - self.prefix_sums[left]
        # return self.prefix_sums[right + 1] - self.prefix_sums[left]


        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)