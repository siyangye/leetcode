class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        found = 0 #matches to t from current substring
        l = 0 # pointer for the beginning of the substring
        min_start = 0
        min_len = float('inf')

        for r,c in enumerate(s):
            if need[c]>0:
                found += 1
            #whether we are not still looking for this character:
            need[c] -=1 #0->-1, init new one if it's not already in need 
            #elif need[char]==0:just ignore it
            if found ==len(t): # we find a substring that fit. 
                while need[s[l]]<0:#crop the substring without excess char
                    # l+=1
                    need[s[l]]+=1
                    l+=1
                curr_len = r-l+1
                if curr_len < min_len:
                    min_start = l
                    min_len = curr_len
                    print(min_len)
            # l+=1 
        if min_len !=float('inf'):
            return s[min_start:min_start+min_len]
        else:
            return ""

        

        
        
        