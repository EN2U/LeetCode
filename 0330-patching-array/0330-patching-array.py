class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        patches = 0

        miss = 1

        while miss <= n:
            if nums and nums[0] <= miss:
                miss += nums[0]
                nums.pop(0)
                continue

            miss *= 2
            patches += 1

        return patches