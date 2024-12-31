class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        max_len = 0
        zeros = 0
        for r in range(len(nums)):#r pointer move while looping 
            if nums[r] == 0:
                zeros += 1
            while zeros > k: #find right position to place l pointer
                if nums[l]==0:
                    zeros -=1 
                l += 1 # l will never be over r -> always: l <= r 
            max_len = max(max_len, r-l+1)
        return max_len
            


            

            
            


            

