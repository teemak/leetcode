class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findBound(first):
            left, right = 0, len(nums) - 1
            bound = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    bound = mid
                    if first:
                        right = mid - 1
                    else:
                        left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return bound

        start = findBound(True)
        if start == -1:
            return [-1, -1]
        end = findBound(False)
        return [start, end]