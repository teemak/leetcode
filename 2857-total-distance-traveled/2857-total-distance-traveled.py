class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        distance = 0
        while mainTank >= 5:
            distance += 50
            mainTank -= 5

            if additionalTank > 0:
                mainTank += 1
                additionalTank -= 1

        distance += mainTank * 10
        return distance