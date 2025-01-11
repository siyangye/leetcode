class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        #count character, frequency.
        if k> len(s):
            return False
        max_str = len(s)
        min_str = 1

        freq = {}
        for char in s:
            freq[char]=freq.get(char,0)+1
        curr_min = 0
        for char,count in freq.items():
            if count%2==1:
                curr_min+=1 #need init?
        min_str = max(curr_min,min_str)
        if min_str<=k<=max_str:
            return True
        return False
                
            

        

        