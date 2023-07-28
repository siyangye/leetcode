class Solution(object):
    def findMaxConsecutiveOnes(self, nums): #nums -> List[num]
        """
        :type nums: List[int]
        :rtype: int
        
        I thought about creating an array, but if you keep update, variable will do. 
        """
        #create a variable to stroe the max/current account of 1s:
        max_account = 0;
        current_account = 0;
       
        for num in nums:
            if num == 1:
                current_account += 1
            else: #num ==0: 
                # max(max_account, current_account);
                max_account = max(max_account, current_account)
                current_account = 0
        
        # edge case: Update max_account again after the loop in case the last element is 1
        max_account = max(max_account, current_account)
        
        return max_account
        
        