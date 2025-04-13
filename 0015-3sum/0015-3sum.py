'''
in
  i
[-1, 0, 1, 2, -1, -4]
     l             r


out
[ [-1, -1, 2], [-1, 0, 1], ]

list of lists
indices store values of elements that sum to zero

plan
1. sort
2. use two pointers
3. left will always be i + 1
4. iterate over each i
5. for each i, use two pointers
6. check the sum of i + left + right, store indices in results
7. move pointers - 
    i. left moves forward when sum needs to increase
    ii. right moves towards middle when sum needs to decrease
8. store the values in global result, not indices

reflections:
1. did not think of duplicate values
2. stored the indices; need to make sure I express the output data type
3. mistake on sorting the nums list, used sorted(nums) but that does nothing unless I store in variable, nums.sort() sorts in place
4. use a set to avoid duplicate triplets

'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = set()
        nums.sort()
        n = len(nums)

        for i in range(0, n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue 

            left, right = i + 1, n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    triplets.add(( nums[i], nums[left], nums[right] ))
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
        return [list(t) for t in triplets]