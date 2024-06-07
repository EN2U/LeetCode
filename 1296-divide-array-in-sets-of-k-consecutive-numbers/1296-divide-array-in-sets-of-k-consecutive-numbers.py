class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k != 0:
            return False
        
        nums.sort()

        invalid = False
        while nums and not invalid:
            current_value = nums[0]
            nums.pop(0)
            for value in range(k - 1):
                current_value += 1

                try:
                    next_idx = nums.index(current_value)
                except ValueError:
                    invalid = True
                    break
                
                nums.pop(next_idx)
            
        return not bool(nums )