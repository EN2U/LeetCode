class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        character_list = ''
        new_list = ''
        for character in s:
            if character not in character_list:
                character_list += character
            else:
                if len(new_list) < len(character_list):
                    new_list = character_list
                    
                character_list = character_list[character_list.find(character) + 1:] + character

        if len(new_list) < len(character_list):
            new_list = character_list

        return len(new_list)