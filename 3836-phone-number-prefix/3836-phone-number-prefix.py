class Solution:
    def phonePrefix(self, numbers: List[str]) -> bool:
        numbers.sort()
        for a, b in pairwise(numbers):
            if b.startswith(a):
                return False

        return True