class Solution:
    def reverse(self, x: int) -> int:

        if not -2**31<=x<=2**31-1:
            return 0

        int_str = str(abs(x))
        sign = -1 if x < 0 else 1
        result = int(int_str[::-1]) * sign

        return result if -2**31<=result<=2**31-1 else 0 