class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        bed = [0] + flowerbed + [0]
        
        count = 0
        consecutive_zeros = 0
        
        for plot in bed:
            if plot == 0:
                consecutive_zeros += 1
            else:  # plot == 1
                # Calculate how many flowers we can plant in this segment
                if consecutive_zeros > 2:
                    # We can place (z-1)//2 flowers in z consecutive zeros between flowers
                    count += (consecutive_zeros - 1) // 2
                    print(count)
                consecutive_zeros = 0
                
        # Add the last segment if it ends with zeros
        if consecutive_zeros > 2:
            count += (consecutive_zeros -1) // 2
            
        return count >= n
        