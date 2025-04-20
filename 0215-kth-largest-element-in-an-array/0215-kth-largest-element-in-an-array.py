class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quickselect(nums, k):
            pivot = random.choice(nums)
            left, mid, right = [], [], []
            # left = mid = right = []

            for num in nums:
                if num < pivot:
                    right.append(num)
                elif num > pivot:
                    left.append(num)
                else:
                    mid.append(num)
                
            if k <= len(left):
                return quickselect(left, k)
            elif len(left) + len(mid) < k:
                return quickselect(right, k - len(left) - len(mid))
            else:
                return pivot

        return quickselect(nums, k)