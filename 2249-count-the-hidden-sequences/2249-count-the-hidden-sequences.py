class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        curr = prefix_min = prefix_max = 0

        for diff in differences:
            curr += diff
            prefix_min = min(prefix_min, curr)
            prefix_max = max(prefix_max, curr)

        start_min = lower - prefix_min
        start_max = upper - prefix_max

        return max(0, start_max - start_min + 1)