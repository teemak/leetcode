class Solution:
    def reverseDegree(self, s: str) -> int:
        total = 0
        z = ord('z')

        for i, char in enumerate(s, 1):
            total += (z - ord(char) + 1) * i
            
        return total
        
         