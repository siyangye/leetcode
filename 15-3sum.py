class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort() 
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue # skip because they have the same value
            # a has to be equal or greater than zero:
            if a <=0: 
                l= i+1
                r = len(nums)-1 
                while l <r:
                    threeSum = a + nums[l]+ nums[r]
                    if threeSum > 0:
                        r= r-1
                    elif threeSum <0:
                        l = l+ 1 
                    else:
                        res.append([a, nums[l], nums[r]])
                        l += 1 
                        while nums[l] == nums[l-1] and l <r: # l within limit r
                            l+= 1
                        # we update the nums value at that time. 
        return res

        
