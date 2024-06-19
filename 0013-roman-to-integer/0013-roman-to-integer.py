class Solution:
    def romanToInt(self, s: str) -> int:
        translation_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        last_value = ""

        total = 0
        for character in s:
            total += translation_dict[character]

            if last_value == 'I' and (character == 'V' or character == 'X'):
                total -= 2 
                continue
            
            if last_value == 'X' and (character == 'L' or character == 'C'):
                total -= 20
                continue

            if last_value == 'C' and (character == 'D' or character == 'M'):
                total -= 200

            last_value = character
        return total