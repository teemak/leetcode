class NumArray:
    def __init__(self, nums: list):
        pass

    def sumRange(self, left: int, right: int) -> int:
        pass


# -----------------------
# 🧪 Sample Test Cases
# -----------------------

# Initialize the NumArray with an example list
nums = [-2, 0, 3, -5, 2, -1]
obj = NumArray(nums)

# Run some test queries
print(obj.sumRange(0, 2))   # Expected: 1
print(obj.sumRange(2, 5))   # Expected: -1
print(obj.sumRange(0, 5))   # Expected: -3

