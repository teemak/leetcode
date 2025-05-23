class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        n = len(nums)
        net = [(nums[i] ^ k) - nums[i] for i in range(n)]
        node = sum(nums)

        net.sort(reverse=True)

        for i in range(0, n, 2):
            if i + 1 == n:
                break

            pair = net[i] + net[i + 1]
            if pair > 0:
                node += pair

        return node