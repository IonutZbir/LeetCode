class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        i = 0
        m = min(len(word1), len(word2))
        while i < m:
            result.append(word1[i])
            result.append(word2[i])
            i += 1
        
        
        if len(word1) < len(word2):
            result.append(word2[len(word1):])
        else:
            print(word1[len(word2):])
            result.append(word1[len(word2):])
        
        return "".join(result)

s = Solution()
s.mergeAlternately("", "pq")