class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        sym = 0
        for x in range(low, high + 1):
            sx = str(x)
            n = len(sx)
            if n % 2 == 0:
                half = n // 2
                fh = [int(c) for c in sx[:half]]
                sh = [int(c) for c in sx[half:]]
                sym += 1 if sum(fh) == sum(sh) else 0
        return sym