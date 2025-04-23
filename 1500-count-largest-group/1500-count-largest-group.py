'''
1. compute digit sum from 1 to n
2. group numbers by their digit sum
3. find the groups with max size
4. return the number of groups of max size
'''
class Solution:
    def countLargestGroup(self, n: int) -> int:
        digit_sums = defaultdict(int)

        for num in range(1, n + 1):
            digit_sum = sum(int(d) for d in str(num))
            digit_sums[digit_sum] += 1

        max_size = max(digit_sums.values())
        return sum(1 for size in digit_sums.values() if size == max_size)
        