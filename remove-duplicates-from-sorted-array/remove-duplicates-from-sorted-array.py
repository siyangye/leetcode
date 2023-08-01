class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #so the second method, we loop while we update/overwrite the origin array
        i = 1 
        j = 0
        for i in range(1,len(nums)): #from 1 to the last item nums[i-1]
            if nums[i] != nums[i -1]:
                j = j+1
                nums[j] = nums [i]
        while j + 1 < len(nums): 
            del nums[j+1]
                    
                    
                 
            