class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        list = []
        while x>0:
            curr_digit = x %10
            x = x //10
            list.append(curr_digit)
        i=0
        j=len(list)-1
        while i<j:
            if list[i]==list[j]:
                i+=1
                j-=1
            else: #list[i]!=list[j]
                return False 
        return True
        