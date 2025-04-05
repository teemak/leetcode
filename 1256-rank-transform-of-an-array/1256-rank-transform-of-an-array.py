class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        uniques = sorted(set(arr))

        rank = {num: i + 1 for i, num in enumerate(uniques)}

        return [rank[num] for num in arr]