class Solution:
    def validPalindrome(self, s: str) -> bool:
        moves = 0
        l=0
        r = len(s)-1 #indexs l,r 
        while l<r:
            if s[l]==s[r]:
                l+=1
                r-=1
            else:
                #check if pop left or right will make it work 
                if l+1 <= r and s[l+1]==s[r]:
                    l+=2
                    r-=1
                    moves +=1
                    continue 
                elif l <=r-1 and s[l]==s[r-1]:
                    l+=1
                    r-=2
                    moves+=1
                else:
                    return False 
            if moves > 1:
                return False
        return True