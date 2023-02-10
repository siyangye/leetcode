#list all of the elements from the [num]

class Solution:

    def Twosum(nums,target):
        #loop: pick the number from first to last
        #len(num) 
        for i in range(len(nums)):
            #loop: pick the number from the 1st one following after:
            for j in range((i+1), len(nums)):
                sum = nums[i] + nums [j]
                if sum == target:
                    return [i,j]
                    
    result = Twosum([1,2,3], 3)
    print(result)



