class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def feasible(threshold):
            count, total = 1, 0
            for num in nums:
                total += num
                if total > threshold:
                    total = num
                    count += 1
                    if count > k:
                        return False
            return True

        left, right = max(nums), sum(nums)
        while left < right:
            mid = (left + right) // 2
            if feasible(mid):
                right = mid
            else:
                left = mid + 1
        return left