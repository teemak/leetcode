class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        def helper(x):
            rotations_top = rotations_bot = 0
            for i in range(len(tops)):
                if tops[i] != x and bottoms[i] != x:
                    return -1
                elif tops[i] != x:
                    rotations_top += 1
                elif bottoms[i] != x:
                    rotations_bot += 1
            return min(rotations_top, rotations_bot)

        res = helper(tops[0])
        if res != -1:
            return res
        elif tops[0] != bottoms[0]:
            return helper(bottoms[0])
        else:
            return -1