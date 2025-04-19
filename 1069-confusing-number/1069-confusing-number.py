class Solution:
    def confusingNumber(self, n: int) -> bool:
        rotate_map = {0: 0, 1: 1, 6: 9, 8: 8, 9: 6}
        original, rotated = n , 0

        while n > 0:
            digit = n % 10
            if digit not in rotate_map:
                return False
            rotated = rotated * 10 + rotate_map[digit]
            n //= 10

        return rotated != original