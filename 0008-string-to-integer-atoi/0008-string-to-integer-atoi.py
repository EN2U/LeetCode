import re
class Solution:
    def myAtoi(self, s: str) -> int:

        match = re.match(r'^\s*[+-]?\d+', s)
        if match:
            result = int(match.group(0)) 
            result = result if -2**31 < result else -2**31
            return result if result < 2**31 -1 else 2**31 -1

        return 0