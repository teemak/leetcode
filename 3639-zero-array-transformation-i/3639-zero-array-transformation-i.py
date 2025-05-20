class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        delta = [0] * (len(nums) + 1)
        for left, right in queries:
            delta[left] += 1
            delta[right + 1] -= 1
        operations = []
        curr = 0

        for d in delta:
            curr += d
            operations.append(curr)
        for ops, tar in zip(operations, nums):
            if ops < tar:
                return False
        return True 