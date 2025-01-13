class Solution:
    def minimumLength(self, s: str) -> int:
        s_dict= {}
        for c in s:
            s_dict[c]=s_dict.get(c,0)+1
        count =0
        for c,freq in s_dict.items():
            if freq <3:
                print(freq)
                count+=freq
            else:
                left_c = (freq-1)%2
                if left_c ==0:
                    count +=1
                else:
                    count +=2
        return count

            
        