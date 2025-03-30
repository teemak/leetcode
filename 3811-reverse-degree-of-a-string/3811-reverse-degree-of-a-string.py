class Solution:
    def reverseDegree(self, s: str) -> int:
        total = 0

        for i, char in enumerate(s, 1):
            total += (ord('z') - ord(char) + 1) * i
            
        return total
        
         