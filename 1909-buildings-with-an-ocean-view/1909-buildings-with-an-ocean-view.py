class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        n = len(heights)
        result = []
        max_height = float('-inf')

        for i in range(n - 1, -1, -1):
            if heights[i] > max_height:
                result.append(i)
                max_height = heights[i]

        return result[::-1]