class Solution:
    def convert(self, s: str, numRows: int) -> str:
        cols = int(len(s))
        matrix = [[None] * cols for _ in range(numRows)]

        valid_string = ""

        if numRows == 1:
            return s

        if numRows == 2:
            for idx in range(0, len(s), 2):
                valid_string += s[idx]

            for idx in range(1, len(s), 2):
                valid_string += s[idx]
            return valid_string

        i = j = 0

        check_diagonal = False
        for character in s:
            matrix[i][j] = character

            if i + 1 < numRows and not check_diagonal:
                i += 1
            elif not check_diagonal:
                check_diagonal = True
                i -= 1
                j += 1
                continue

            if i - 1 > 0 and check_diagonal:
                i -= 1
                j += 1
            elif check_diagonal:
                check_diagonal = False
                i = 0
                j += 1

        valid_string = ""
        for row in matrix:
            valid_string += "".join(filter(None, row))

        return valid_string