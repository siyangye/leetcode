class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        
        # new = []
        # for i in range(len(arr) - 1): #range(0,6) is equal to range(6):[0,1,2,3,4,5]
        #     new.append(max(arr[i + 1:])) ## Slice from index 2 to 5 (inclusive) slice_result = my_list[2:6]
        # new.append(-1)
        # return new
        #method 1: exceed time limit again
        
        #method 2:
        #initial max = -1 
        #reverse iteration
        #new max = max(oldmax, arr[i])
        
        rightMax = -1 
        
        for i in range(len(arr)-1, -1,-1):
            arr[i] = max(rightMax, arr[i]) #之前比较的
            rightMax = arr[i] #更新rightMax的值
            
        arr.append(-1)
        return arr[1:]
        
        