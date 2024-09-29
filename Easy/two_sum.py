# Problem - https://leetcode.com/problems/two-sum/

from typing import List

class Solution:
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # [3, 2, 4]
        # 
        # "0" -> "1"
        # "1" -> "0"
        # "2" -> "2"
        # 
        # [2, 3, 4]
        
        m = {}
        
        for i, n in enumerate(nums):
            compl = target - n
            
            if compl in m:
                return [m[compl], i]
            
            m[n] = i
