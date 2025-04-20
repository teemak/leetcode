class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]  # 3, 2
        # print(heap)
        heapq.heapify(heap)

        for num in nums[k:]: #[2->]
            if num > heap[0]:
                heapq.heappushpop(heap, num)

        return heap[0] 