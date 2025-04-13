class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        counter = Counter(deliciousness)
        res = 0
        mod = 10 ** 9 + 7

        for val, freq in counter.items():
            if val == 0:
                continue
            closest = 2 ** math.ceil(math.log2(val))
            diff = closest - val

            if closest == val:
                res += freq * (freq - 1) // 2
            
            res += freq * counter[diff]
        
        return res % mod
