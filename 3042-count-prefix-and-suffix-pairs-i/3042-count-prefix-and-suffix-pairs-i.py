class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def isPrefixAndSuffix(str1:str,str2:str) -> bool:
            n = len(str1)
            if str1 == str2[:n] and str1 == str2[-n:]:
                return True
            return False
        count = 0
        for i in range(len(words)-1):
            for j in range(i+1,len(words)):
                if isPrefixAndSuffix(words[i],words[j]):
                    count+=1
                    print(words[i],words[j])
        return count 

        
            