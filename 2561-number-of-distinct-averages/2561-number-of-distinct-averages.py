'''
in______
[4,1,4,0,3,5]
       x   x


--------
out_____
2

solutions:
1. two pointers

plan:
1. sort the list, ascending order
2. declare 2 pointers
3. form pairs
4. compute avg
5. move pointers toward middle
'''
class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        res = set()
        nums = sorted(nums)
        left, right = 0, len(nums) - 1

        while left < right:
            res.add((nums[left] + nums[right]) / 2)
            left += 1
            right -= 1
        
        return len(res)
