class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)
        i = 0
        j =0
        while i < n:
            while j < n: 
                if fruits[i] <= baskets[j]:
                    baskets[j] = 0
                j += 1
            i += 1
        count = 0
        for j in range(len(baskets)):
            if baskets[j] !=0:
                count += 1
        return count
