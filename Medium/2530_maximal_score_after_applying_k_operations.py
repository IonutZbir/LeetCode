from math import ceil

# TODO: Da usare l' heap coglione!!!

class Solution:
    def maxKelements(self, nums: list[int], k: int) -> int:
        s = 0
        j = 0
        nums.sort()
        for _ in range(k):
            m = nums[j]
            s += m
            nums[j] = ceil(nums[j] / 3)
            
            if nums[j] < nums[j + 1]:
                j += 1    
        
        return s
                        