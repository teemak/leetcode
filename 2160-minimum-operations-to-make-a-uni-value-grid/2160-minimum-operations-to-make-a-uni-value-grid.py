class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        nums = []
        result = 0

        for row in grid:
            for num in row:
                nums.append(num)

        nums.sort()

        length = len(nums)

        final = nums[length // 2]

        for number in nums:
            if number % x != final % x:
                return -1
            result += abs(final - number) // x

        return result