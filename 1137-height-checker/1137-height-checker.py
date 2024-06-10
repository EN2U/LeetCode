class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_heights = sorted(heights)

        result = 0
        for i in range(len(heights)):
            result += heights[i] != sorted_heights[i]

        return result