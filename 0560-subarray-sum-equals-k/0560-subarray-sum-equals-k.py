class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        sum = 0
        dict = {0: 1}

        for n in nums:
            sum += n
            remaining = sum - k

            if remaining in dict:
                res += dict[remaining]
            
            dict[sum] = dict.get(sum, 0) + 1
        
        return res
