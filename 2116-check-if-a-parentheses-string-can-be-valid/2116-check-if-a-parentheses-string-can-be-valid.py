class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s)%2==1:
            return False 
        left,right,flex=0,0,0
        for i in range(len(s)):
            if locked[i]=='1': #1 or '1'
                if s[i]==")":
                    right += 1
                else:
                    left += 1
            if locked[i]=='0':
                flex += 1
            if left +flex < right:
                return False
        for i in range(len(s)-1,-1,-1):
            if locked[i]=='1': #1 or '1'
                if s[i]==")":
                    right += 1
                else:
                    left += 1
            if locked[i]=='0':
                flex += 1
            if right +flex < left:
                return False
        return True

        
        