class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefix =[0]*(len(s)+1)
        for shift in shifts:
            start_ind = shift[0]
            end_ind = shift[1]
            pos = shift[2]
            if pos==1:
                prefix[start_ind] +=1
                prefix[end_ind+1] -=1
            else: #pos ==0
                prefix[start_ind]-=1
                prefix[end_ind+1]+=1
        prefix_sum = 0
        res = ''
        for i in range(len(s)):
            prefix_sum+= prefix[i]
            #orginal char:
            curr_ind = (ord(s[i])-ord('a')+prefix_sum)%26
            curr_char = chr(ord('a')+curr_ind)
            res+=curr_char
        return res
