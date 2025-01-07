class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        # clarify on edge case: if we find nothing -> return empty string?
        # all of the strings are unique? 
        #[mass,as,hero,superhero,superheromario,]
        res =[]
        for i in range(len(words)): 
            for j in range(len(words)):
                if i != j and words[j] in words[i]:
                    res.append(words[j]) 
        print(set(res)) #consider the case where a string could be a substring for multiple strings in the list. 
        return list(set(res))