class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)
        count = 0
        
        for i in range(n):
            placed = False
            for j in range(len(baskets)):
                if fruits[i] <= baskets[j]:
                    baskets[j] = 0
                    placed = True
                    break
            
            if not placed:
                count += 1
        
        return count
