class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        major, bit = 0, 1

        for i in range(31):
            count = sum(bool(num & bit) for num in nums)
            if count > n // 2:
                major += bit
            bit = bit << 1

        neg = sum(num < 0 for num in nums) > (n // 2)

        if neg:
            major -= bit
        
        return major
