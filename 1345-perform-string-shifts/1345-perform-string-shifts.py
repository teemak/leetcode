class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        net_shift = 0
        for direction, amount in shift:
            if direction == 0:
                net_shift -= amount
            else: net_shift += amount
        n = len(s)
        net_shift %= n

        return s[-net_shift:] + s[:-net_shift] if net_shift else s