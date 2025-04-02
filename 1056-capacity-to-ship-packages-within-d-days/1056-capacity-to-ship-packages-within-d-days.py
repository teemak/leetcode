class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def feasible(capacity):
            d, total = 1, 0
            for weight in weights:
                total += weight
                if total > capacity:
                    total = weight
                    d += 1
                    if d > days:
                        return False
            return True

        left, right = max(weights), sum(weights) 
    
        while left < right:
            mid = (right + left) // 2
            if feasible(mid):
                right = mid
            else:
                left = mid + 1
        return left
