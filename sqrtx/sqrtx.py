class Solution:
    def mySqrt(self, x: int) -> int:
        l= 0
        r = x 
        
        while l <= r:
            mid = l + (r-l)//2 
            
            if mid **2 > x:
                r = mid - 1
            elif mid **2 < x:
                l = mid + 1 
                res = mid #难点在这里，round down to the closest squared int. 
            elif mid ** 2 == x:
                return mid 
                
        return res #return squared result here. 
                
        
        