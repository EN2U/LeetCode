class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        final_string = ""
        new_string = ""
        word_found = False
        for character in sentence:
            if character == " ":
                final_string += " "
                word_found = False
                new_string = ""
                continue

            if not word_found:
                new_string += character
                final_string += character

                if new_string in dictionary:
                    word_found = True


        return final_string
