'''
input. 
 nums = [3, 0, 1]


output. 
2


plan - create a set of nums and remove as we iterate, return last element in set
constraints:


'''
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        seen = set(range(n + 1))

        for num in nums:
            if num in seen:
                seen.remove(num)
                
        return seen.pop()