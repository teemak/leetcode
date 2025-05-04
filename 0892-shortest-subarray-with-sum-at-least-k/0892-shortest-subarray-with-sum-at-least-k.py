class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix = [0]
        for i in range(n):
            prefix.append(prefix[i] + nums[i])

        dq = deque()
        min_len = n + 1

        for j in range(n + 1):
            while dq and prefix[j] - prefix[dq[0]] >= k:
                min_len = min(min_len, j - dq.popleft())
            while dq and prefix[j] <= prefix[dq[-1]]:
                dq.pop()
            dq.append(j)

        return min_len if min_len <= n else -1