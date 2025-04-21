class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"

        if n == 2:
            return "11"

        s = self.countAndSay(n - 1)
        
        s = self.rle(s)

        return s
    
    def rle(self, s: str) -> str:
        new_s = ""

        i = 1
        n = len(s)
        count = 1
        while i < n:
            if s[i] == s[i - 1]:
                count += 1 
            else:
                new_s += str(count) + s[i - 1]
                count = 1
            i += 1

        new_s += str(count) + s[-1]

        return new_s

solver = Solution()
n = 4
ret = solver.countAndSay(n)
print(ret)

# solver.rle("11")