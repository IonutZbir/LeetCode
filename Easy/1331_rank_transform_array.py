# Problem: https://leetcode.com/problems/rank-transform-of-an-array

from typing import List

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        list_set = set(arr)
        list_set = list(list_set)
        sorted_arr = sorted(list_set)
        
        ranks = {}
        
        r = 1
        for i in range(len(sorted_arr)):
            ranks[sorted_arr[i]] = r
            r += 1
        
        r = []
        for num in arr:
            r.append(ranks.get(num))
        
        return r
        

s = Solution()
print(s.arrayRankTransform([37,12,28,9,100,56,80,5,12]))