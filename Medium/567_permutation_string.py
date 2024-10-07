class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        
        freq_s1 = {}
        for x in s1:
            freq_s1[x] = freq_s1.get(x, 0) + 1
        
        i,j = 0, n1 - 1
        
        while j < n2:
            freq_s2 = {}
            window = s2[i:j + 1]
            for x in window:
                freq_s2[x] = freq_s2.get(x, 0) + 1
            
            if freq_s2 == freq_s1:
                return True
            
            i += 1
            j += 1
            
            
        return False

        
        

s = Solution()
k = s.checkInclusion("ab", "eidboa")
print(k)
            