# Problem https://leetcode.com/problems/maximum-swap/

class Solution:
    def maximumSwap(self, num: int) -> int:
        ns = list(str(num))
        
        m = str(max([int(x) for x in ns]))
        
        if m == ns[0] and len(ns) > 1:
            m = str(max([int(x) for x in ns[1:]]))
        
        indx = ns.index(m)
        t = ns[0]
        ns[0] = m
        ns[indx] = t
        
        return int("".join(ns))
                
