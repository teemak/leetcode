class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        mod = 10 ** 9 + 7
        max_val = max(deliciousness)
        max_sum = 2 ** max_val
        pows_of_2 = [1 << i for i in range(22)] 
        count = defaultdict(int)
        pairs = 0

        for val in deliciousness:
            for target in pows_of_2:
                diff = target - val
                pairs += count[diff]
            count[val] += 1

        return pairs % mod
        