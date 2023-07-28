# Input: nums = [12,345,2,6,7896]
# Output: 2
class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        evenDigitNumbers = 0;
        for each numbers count there digit
        if it is even digit, edn += 1;
        
        """
#         #method 1: counting cases one by one:
#         evenDigitNumbers = 0
#         for num in nums: #1,10(2),100,1000(4),10000,100000(6)
#             if num >= 10 and num < 100:
#                 evenDigitNumbers += 1;
#             if num >= 1000 and num < 10000:
#                 evenDigitNumbers += 1;
#             if num == 100000:
#                 evenDigitNumbers += 1;
                
#         return evenDigitNumbers
    
    
#         #method 2: keep divid numbers by 10 to get the digits
#         evenDigitCounts = 0
#         for num in nums:
#             digit = 1 #starting point
#             while num >= 10:
#                 num = num//10 
#                 digit += 1
#             if digit %2 ==0:
#                 evenDigitCounts += 1
#         return evenDigitCounts
    
        #method 3: format num to string, and count length of string = digits.
        evenDigitCounts = 0
        for num in nums:
            digit = len(str(num))
            if digit % 2 == 0:
                evenDigitCounts += 1
        return evenDigitCounts
                
        