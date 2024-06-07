class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        new_list = nums1 + nums2

        new_list.sort()

        length = len(new_list)

        if length % 2 == 0:
            return (new_list[length // 2 - 1] + new_list[length // 2]) / 2
        return new_list[length // 2]
