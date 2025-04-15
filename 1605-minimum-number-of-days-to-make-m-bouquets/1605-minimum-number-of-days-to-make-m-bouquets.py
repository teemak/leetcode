class Solution:
    def helper(self, bloomDay, mid, k):
        bouquets = count = 0

        for day in bloomDay:
            if day <= mid:
                count += 1
            else:
                count = 0
            
            if count == k:
                bouquets += 1
                count = 0

        return bouquets

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1
        start = 0
        end = max(bloomDay)
        minDays = -1

        while start <= end:
            mid = (start + end) // 2

            if self.helper(bloomDay, mid, k) >= m:
                minDays = mid
                end = mid - 1
            else:
                start = mid + 1

        return minDays
