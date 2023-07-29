class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        
        for sort list: o is the possible smallest ones
        decide the biggest
        """
        #method 1: 
        sort = [] #from largest -> smallest 
        l,r = 0, len(nums) -1
        while l <= r: #they are not across each other
            if nums[l]* nums[l] > nums[r] *nums[r]: 
                sort.append(nums[l] *nums[l])
                l = l +1 
            else:
                sort.append(nums[r] *nums[r])
                r = r-1 
        
        return sort[::-1] #reverse
             
# #     #method 2: list it one by one 
#         sort = []
#         for num in nums:
#             k = num **2 
            
#             i = 0
#             if not sort or sort[-1] <= k:
#                 sort.append(k)
#             else:
#                 sort.append(0) #append first
#                 while i < len(sort) and sort[i] <= k:
#                     i = i+1
#                 #when: sort[i] >k, break the while loop 
#                 # move the latter list forward, but you have to do it backwards, or it will get overwrite. 
#                 j = len(sort) -1
#                 while j > i:
#                     sort[j] = sort[j-1]
#                     j = j-1
#                 sort[i] = k
            

#         return sort 
        
#         sorted = []

#         for num in nums:
#             #square it 
#             sqr = num ** 2 

#             # Find the proper position to place the new square
#             i = len(sorted);
#             while i > 0 and sorted[i - 1] > sqr:
#                 i = i - 1

#             # Expand the container first!!!
#             sorted.append(0)

#             # For all those after the position, move one position
#             # afterward; and, moving should start from the end!!!
#             j = len(sorted) - 1
#             while j > i:
#                 sorted[j] = sorted[j - 1]
#                 j = j - 1

#             # Plase the new square in the proper position
#             sorted[i] = sqr

#         return sorted

                
            
        
            
        