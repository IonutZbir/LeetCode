from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        if len(flowerbed) > 1:
            if flowerbed[0] == 0 and flowerbed[1] == 0:
                flowerbed[0] = 1
                n -= 1
        
            if flowerbed[-2] == 0 and flowerbed[-1] == 0:
                flowerbed[-1] = 1
                n -= 1

            print(flowerbed)

            for i in range(2, len(flowerbed) - 2):
                if flowerbed[i] == 0 and flowerbed[i + 1] == 0 and flowerbed[i - 1] == 0:
                    flowerbed[i] = 1
                    n -= 1
        else:
            if flowerbed[0] == 0:
                n -= 1

        return n <= 0