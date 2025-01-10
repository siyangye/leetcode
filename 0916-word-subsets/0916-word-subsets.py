class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        frequency=defaultdict(int)
        for a in words1:
            for b in words2:
                if b in a:
                    frequency[a]+=1
        res =[]
        n = len(words2)
        for i in frequency:
            if frequency[i]==n:
                res.append(i)
        return res


        