class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """ 
        
       
        i = 0
        while i < len(arr):
            if arr[i] == 0:
                arr.insert(i+1,0)
                del arr[len(arr) -1]
                i = i+2 #since you duplicate, you have to the next next one. 
            else:
                i = i+1 
            
        
    
        