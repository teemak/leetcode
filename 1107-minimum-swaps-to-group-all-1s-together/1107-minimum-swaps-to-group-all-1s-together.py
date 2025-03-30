class Solution:
    def minSwaps(self, data: List[int]) -> int:
        ones = sum(data)
        count = res = left = right = 0

        while right < len(data):
            count += data[right]
            right += 1

            if right - left > ones:
                count -= data[left]
                left += 1

            res = max(res, count)
        return ones - res