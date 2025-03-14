class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        bed = [0]
        for fb in flowerbed:
            bed.append(fb)
        bed.append(0)
        # print(bed)
        curr = 0
        count = [] #zero
        for i in range(len(bed)):
            if bed[i] == 0:
                curr += 1
            else:
                count.append(curr)
                #reset:
                curr = 0
        count.append(curr)
        max_count = 0
        print(count)
        for c in count:
            if c >= 3:
                c -= 2
                if c % 2 == 0:
                    max_count += c // 2
                else:
                    max_count += c// 2 + 1
        print(max_count)
        return max_count >= n

            
