'''
in:  [12,6,1,2,7]

(0,2,4) -> (12 - 1 * 7)

out: 77

max value over (i,j,k) i < j < k indices

return 0 else max(i, j, k)

constraints:
1. sequence matters
2. i - j * k (order of operations matter), greedy won't work
3. input length will always be valid up to 100
4. values are 1 to 10_000_000

plan:                                                       time          space
sliding window
1. try to get the largest difference between i - j          O(n)          O(1)
    - 2 (i)passes, get the min, (ii)get product of diff

steps:                  step
 i
[12, 6, 1, 2, 7]        6    * [1, 12, 42]
     j                  11   *    [22, 77]
                        10   *    [70]
                        5 (not valid)

** need to iterate i to find largest diff                    
   i    j
[1,10,3,4,19]           7    * [28, 133]
                        6
                        
will the largest difference always contain the largest product?
j can only iterate up to last element

implementation:
1. iterate i
2. iterate j, where j is i + 1 up to len(input) - 1
3. iterate k, where k is j + 1 up to len(input)

'''
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        result = 0
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    result = max(result, (nums[i] - nums[j]) * nums[k])

        return result
        