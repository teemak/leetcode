class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prefix_sums = [0]
        for i in range(len(nums)):
            self.prefix_sums.append(nums[i] + self.prefix_sums[i])        

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_sums[right + 1] - self.prefix_sums[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)