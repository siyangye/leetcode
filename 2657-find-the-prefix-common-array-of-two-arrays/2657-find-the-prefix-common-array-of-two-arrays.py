class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        if len(A)==1:
            return [1]
        ind_dict ={}
        for i in range(len(A)):
            # print(i)
            if A[i] not in ind_dict:
                ind_dict[A[i]]=i
                print(i)
            if A[i] in ind_dict:
                curr_ind = ind_dict[A[i]]
                if i > curr_ind:
                    ind_dict[A[i]]=i
            if B[i] not in ind_dict:
                ind_dict[B[i]]=i
            if B[i] in ind_dict:
                curr_ind = ind_dict[B[i]]
                if i > curr_ind:
                    ind_dict[B[i]]=i 
        count = {}
        for c,ind in ind_dict.items():
            # print(c)
            count[ind]=count.get(ind,0)+1
        res = []
        curr=0
        for j in range(len(A)):
            if j in count:
                curr+= count[j]
            res.append(curr)
        return res
            
        
        