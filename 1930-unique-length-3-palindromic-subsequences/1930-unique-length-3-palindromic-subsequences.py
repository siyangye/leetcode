class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        # for i in range(len(s)-2):
        count = 0
        first_pos = {}
        last_pos = {}
        for i,c in enumerate(s):
            if c not in first_pos:
                first_pos[c]=i
            last_pos[c]=i
        for c in first_pos:
            print(c)
            if first_pos[c]+1 < last_pos[c]:
                unique =set()
                l_index = first_pos[c]
                r_index = last_pos[c]
                # mid = l_index
                for mid in range(l_index+1,r_index):#左闭右开
                    if mid not in unique:
                        unique.add(s[mid]) #?
                        # print(mid)
                count += len(unique)
                    # mid +=1
        return count

