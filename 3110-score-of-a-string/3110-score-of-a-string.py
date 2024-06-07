class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        for idx, character in enumerate(s[1:]):
            score += abs(ord(s[idx]) - ord(character))

        return score