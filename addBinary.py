class Solution:
    def addBinary(self, a: str, b: str) -> str:
        #initialize pointer 
        i, j = len(a) -1, len(b) -1
        tempSum = 0 #empty int
        result = [] #empty string
        
        while max(i,j) >=0:
            if i >= 0:
                num_a = int(a[i]) * (2**i)
            else:
                num_a = 0
            if j >= 0:
                num_b = int(b[j]) *(2**j)
            else:
                num_b = 0
            tempSum += num_a +num_b 
            i-= 1
            j-= 1
        
        # return:tempSum
        #save each int:
        while tempSum > 0:
            bit = tempSum % 2 
            result.append(str(bit))
            tempSum //= 2 
        result = ''.join(result[::-1]) #reverse the list 
        # resultInString = str(result)
        return result
        
            
            
        
