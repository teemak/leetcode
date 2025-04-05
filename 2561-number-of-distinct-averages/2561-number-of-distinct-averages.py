class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
       a, n = sorted(nums), len(nums) // 2
       res = len({a[i] + a[~i] for i in range(n)}) 
       return res