'''
in [1, 0, -1, 0, -2, 2]

out
[
    [-2, -1, 1, 2],
    [-2,  0, 0, 2],
    [-1,  0, 0, 1],
]

return => list of values that sum to target
1. store the values and index in a dict
2. iterate the nums list
3. for every pair, use two pointers that will calculate the sum
4. if the sum is equal to the target - add the values to the dict

plan:
sort the nums list
store the values in a set
iterate and store the set

 i  i   i  
[1, 0, -1, 0, -2, 2]
           j   
               k  k
'''
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        result = set()

        for i in range(n - 3):
            for j in range(i + 1, n - 2):
                # must be reset for each new pair
                seen = set()
                for k in range(j + 1, n):
                    diff = target - nums[i] - nums[j] - nums[k]
                    if diff in seen:
                        result.add((nums[i], nums[j], nums[k], diff))
                    seen.add(nums[k])
    
        return [list(quads) for quads in result]