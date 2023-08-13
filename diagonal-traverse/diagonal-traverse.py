class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        num_rows, num_cols = len(matrix), len(matrix[0])
        diagonals = [[] for _ in range(num_rows+ num_cols -1)]
        #create a 2d list to stroe all elements:
        for i in range(num_rows):
            for j in range(num_cols):
                #难点: 每个element分别append到对应的rows[i+j]中
                diagonals[i+j].append(matrix[i][j]) 
        #convert the 2d list into diagonal sequence
        res = diagonals[0] #store the first row 
        for p in range(1,len(diagonals)): #reverse the rest of the rows
            if p % 2 ==0:
                #reverse even rows:
                res.extend(diagonals[p][::-1]) #extend element, append whole list
            else:
                res.extend(diagonals[p])
        #return out of the loop
        return res
            
        