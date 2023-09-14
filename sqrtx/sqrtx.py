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
                res = mid
            elif mid ** 2 == x:
                return mid
                
        return res
                
        
        