class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        m = len(flowerbed)
        for i in range(m):
            if i - 1 < 0 and i + 1< m:
                if flowerbed[i + 1] == 0 and flowerbed[i] == 0:
                    flowerbed[i] = 1
                    count += 1
            elif i + 1 >= m and i - 1>= 0:
                if flowerbed[i - 1] == 0 and flowerbed[i] == 0:
                    flowerbed[i] = 1
                    count += 1
                    print(count)
            elif i + 1 < m and i - 1>= 0:
                if flowerbed[i - 1]== 0 and flowerbed[i + 1] ==0 and flowerbed[i] == 0:
                    flowerbed[i] = 1
                    count+= 1
            elif i+ 1 == m and i - 1 == -1 and flowerbed[i]== 0:
                count += 1
        print(count)
        print(n)
        return count >= n

        