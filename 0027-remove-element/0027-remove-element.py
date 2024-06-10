class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        total_ocurrences = len(nums)
        i = k = 0
        new_array = []

        while i < len(nums):
            if not nums[i] == val:
                nums[k] = nums[i]
            else:
                k -= 1
                total_ocurrences -= 1    
            i += 1
            k += 1

        return total_ocurrences