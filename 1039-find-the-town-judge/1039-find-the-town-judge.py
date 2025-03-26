class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trust_counts = [0] * (n + 1)

        for u, v in trust:
            trust_counts[u] -= 1
            trust_counts[v] += 1
            
        for person in range(1, n + 1):   
            if trust_counts[person] == n-1:
                return person
        return -1