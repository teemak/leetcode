class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = collections.Counter(answers)
        result = sum(-v % (k + 1) + v for k, v in count.items())
        return result