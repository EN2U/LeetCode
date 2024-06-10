class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_heights = sorted(heights)

        result = 0
        for i in range(len(heights)):
            result += 0 if heights[i] == sorted_heights[i] else 1

        return result