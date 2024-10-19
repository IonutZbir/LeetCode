class Solution:
    def minimumSteps(self, s: str) -> int:
        s = list(s)  
        i = 0
        j = len(s) - 1
    
        swaps = 0
        while i < j:
            if s[i] == "1" and s[j] == "0":
                s[i], s[j] = s[j], s[i]
                swaps += j - i
                i += 1
                j -= 1
            elif s[i] == "0":
                i += 1
            elif s[j] == "1":
                j -= 1
            else:
                i += 1
                j -= 1

        return swaps
