from math import sqrt

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i = 0
        while i**2 <= c:
            check_value = sqrt(c - i**2)
            if not check_value.is_integer():
                i += 1
                continue

            return True



        return False