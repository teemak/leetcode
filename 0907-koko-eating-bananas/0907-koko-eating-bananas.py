class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        pq = []
        min_k, max_k = 1, max(piles)

        for p in piles:
            heapq.heappush(pq, -p)

        def time(k):
            t = 0
            for p in piles:
                t += math.ceil(p/k)
            return t

        while min_k < max_k:
            k = (min_k + max_k) // 2
            t = time(k)
            if t <= h:
                max_k = k
            else:
                min_k = k + 1

        return min_k


        return -pq[0][0]


