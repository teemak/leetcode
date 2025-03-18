class Solution:
    def maxIncreasingGroups(self, usageLimits: List[int]) -> int:
        n = len(usageLimits)
        val, size = 0, 0
        freq = [0] * n
        avail = [0] * n

        for num in usageLimits:
            if num > n:
                freq[0] += 1
            else:
                freq[-num] += 1

        for count in freq:
            count += val
            val = count
            while count > size:
                size += 1
                count -= size - avail.pop()
            avail.append(count)

        return size