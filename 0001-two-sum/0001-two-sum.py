class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapped_nums = {num: idx for idx, num in enumerate(nums)}
    
        for idx, value in enumerate(nums):
            complement = target - value
            if complement in mapped_nums and mapped_nums[complement] != idx:
                return [idx, mapped_nums[complement]]