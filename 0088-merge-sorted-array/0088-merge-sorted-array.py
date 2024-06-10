class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        new_array = sorted(nums1[:m] + nums2[:n])

        for i in range(len(new_array)):
            nums1[i] = new_array[i]