class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def condition(k):
            time = 0
            for pile in piles:
                hours = math.ceil(pile/k)
                time += hours
            return time <= h

        left, right = 1, max(piles)

        while left < right:
            mid = (right + left) // 2
            if condition(mid):
                right = mid
            else:
                left = mid + 1
        return left