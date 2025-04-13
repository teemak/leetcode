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
        nums.sort()
        triplets = set()
        l1 = []
        for idx, key in enumerate(nums):
            if key not in l1:
                l1.append(key)
            else:
                continue
            i = 0
            j = len(nums) - 1
            while i < j:
                if i == idx:
                    i += 1
                    continue
                elif j == idx:
                    j -= 1
                    continue
                else:
                    sums = nums[i] + nums[j]
                    if sums == -key:
                        triplets.add(tuple(sorted([key, nums[i], nums[j]])))
                        i += 1
                        j -= 1
                    elif sums > -key:
                        j -= 1
                    else:
                        i += 1
        l = []
        for val in triplets:
            l.append(list(val))
        return l
