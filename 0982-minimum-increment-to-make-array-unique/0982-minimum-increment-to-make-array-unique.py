class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()

        previous_number = nums[0]
        total_moves = 0

        for i in range(1, len(nums)):
            if nums[i] <= previous_number:
                previous_number += 1
                total_moves += previous_number - nums[i]
            else:
                previous_number = nums[i]

        return total_moves