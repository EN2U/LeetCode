class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        color_hashmap = {
            0: 0,
            1: 0,
            2: 0,
        }

        for num in nums:
            color_hashmap[num] += 1    
        
        new_list = sum([[key] * value for key, value in color_hashmap.items()], [])

        for idx in range(len(nums)):
            nums[idx] = new_list[idx]