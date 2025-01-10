class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        #make a dict, based on words2, update how many letters I need for a word in word1 to meet requirement. 
        b_dict=defaultdict(int)
        for b in words2:
            curr_dict= {}
            for char in b:
                curr_dict[char] = curr_dict.get(char,0)+1
            for char,freq in curr_dict.items():
                # char,freq=curr_dict[i]
                b_dict[char]=max(b_dict[char],freq)
        res=[]
        #for each word in word1, check if it meet the requirement:
        for a in words1:
            a_dict={}
            for char in a:
                a_dict[char]=a_dict.get(char,0)+1
            for char,freq in b_dict.items():
                is_valid = True
                if char not in a_dict or a_dict[char]<freq:
                    is_valid= False
                    break
            if is_valid:
                res.append(a)
        return res

            



        