# Problem: https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

# S1 = "0"
# Si = S_(i - 1) + "1" + reverse(invert(S_(i - 1))) for i > 1

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s = self.create(n)
        return s[k - 1]
    
    def create(self, n: int) -> str:
        if n == 1:
            return "0"
        
        return self.create(n - 1) + "1" + self.reverse(self.invert(self.create(n - 1)))
    
    def reverse(self, s: str) -> str:
        return s[::-1]
    
    def invert(self, s: str) -> str:
        return "".join(["1" if bit == "0" else "0" for bit in s])
    