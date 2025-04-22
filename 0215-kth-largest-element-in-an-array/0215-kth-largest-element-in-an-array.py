class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def qs(arr, k):
            pivot = random.choice(arr) 

            l = [x for x in arr if x > pivot]
            m = [x for x in arr if x == pivot]
            r = [x for x in arr if x < pivot]

            left, mid = len(l), len(m)

            if k <= left:
                return qs(l, k)
            elif k > left + mid:
                return qs(r, k - left - mid)
            else:
                return pivot
        
        return qs(nums, k)