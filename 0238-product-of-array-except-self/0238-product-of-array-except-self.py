class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l=[1]
        left = 1
        for i in range(len(nums)-1):
            left = left*nums[i]
            l.append(left)
        print(l)
        r =[1]
        right = 1
        for j in range(len(nums)-1,0,-1):
            right =right*nums[j]
            r.append(right)
        r = r[::-1] 
        print(r)
        res = []
        for i in range(len(nums)):
            curr = l[i]*r[i]
            res.append(curr)
        return res