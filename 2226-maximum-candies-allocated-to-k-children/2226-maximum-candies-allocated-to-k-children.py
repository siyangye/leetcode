class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        max_count = sum(candies) // k
        if max_count ==0:
            return 0
        while max_count > 0:
            curr_count = 0
            for candy in candies:
                curr_count += candy // max_count
            # print(curr_count)
            if curr_count >= k:
                # print(max_count)
                return max_count
            else:
                max_count -= 1
                print(max_count)
        return max_count
            
                
        