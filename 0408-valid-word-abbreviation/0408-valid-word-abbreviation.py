class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i,j = 0,0
        while i <len(word) and j < len(abbr):
            if word[i]==abbr[j]:
                i+=1
                j+=1
                continue
            if not abbr[j].isdigit() or abbr[j]=='0':
                return False
            else:
                count = 0
                while j<len(abbr) and abbr[j].isdigit(): #when to exit this loop:next element in abbr is not digit OR there is no more element in abbr anymore. 
                    count = count*10+ int(abbr[j])
                    j+=1
                i+= count
        return i==len(word) and j==len(abbr)

                                                                                     