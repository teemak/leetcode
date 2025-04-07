'''
input: nums = [100, 4, 200, 1, 3, 2]
                    1234 => 4
                    longest consecutive subsequence

                [0,3,7,2,5,8,4,6,0,1]
                 012345678 => 9
output: 4

1. sort list
2. iterate pointer while updating global counter
3. must be O(n) because we need to check every element

constraints:
duplicate numbers - 
can use a set or condition check
need to work backwards so there is no index out of range

'''
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        result = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_consecutive = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_consecutive += 1
                result = max(current_consecutive, result)

        return result

            
        