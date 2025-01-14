class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if not firstList or not secondList:
            return []
        p1,p2=0,0
        res = []
        while p1 <len(firstList) and p2<len(secondList):
            start1,end1=firstList[p1]
            start2,end2=secondList[p2]
            if max(start1,start2)<=min(end1,end2):
                res.append([max(start1,start2),min(end1,end2)])
                if end1>end2:
                    p2+=1
                elif end1 <end2:
                    p1+=1
                else:
                    p1+=1
                    p2+=1
            elif end1<start2:
                p1+=1
            elif end2<start1:
                p2+=1
        return res
        
        