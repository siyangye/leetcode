class Solution:
    def myPow(self, x: float, n: int) -> float:
        # if x == 0:
        #     return 0
        # elif n == 0:
        #     return 1
        # # elif n == 1:
        # #     return x 
        # elif n >= 1:
        #     res = 1 
        #     while n >=1:
        #         res *= x
        #         n -= 1 
        #     return res
        # # elif n == -1:
        # #     return 1/x
        # elif n <= -1:
        #     power = -1 *n
        #     res = 1
        #     while power >=1:
        #         res *= x
        #         power-= 1
        #     return 1/res 
        return pow(x,n)



        