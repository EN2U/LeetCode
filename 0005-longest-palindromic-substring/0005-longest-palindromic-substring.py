class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_palindrome = s[0]
        characters_to_evaluate = s[0]
        for character in s[1:]:
            characters_to_evaluate += character
            longest_palindrome = self.check(
                characters=characters_to_evaluate, longest_palindrome=longest_palindrome
            )
        return longest_palindrome

    def check(self, characters: str, longest_palindrome: str):
        i = -1
        j = len(characters)
        while i + 1 < j - 1:
            j -= 1
            i += 1
            if not characters[i] == characters[j]:
                characters = characters[1:]
                j = len(characters)
                i = -1

        if len(longest_palindrome) < len(characters):
            longest_palindrome = characters

        return longest_palindrome