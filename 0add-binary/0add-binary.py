# class Solution:
#     def addBinary(self, a: str, b: str) -> str:
#         #initialize pointer 
#         i, j = len(a) -1, len(b) -1
#         tempSum = 0 #empty int
#         result = [] #empty string
        
#         while max(i,j) >=0:
#             if i >= 0:
#                 num_a = int(a[i]) * (2**i)
#             else:
#                 num_a = 0
#             if j >= 0:
#                 num_b = int(b[j]) *(2**j)
#             else:
#                 num_b = 0
#             tempSum += num_a +num_b 
#             i-= 1
#             j-= 1
        
#         # return:tempSum
#         #save each int:
#         while tempSum > 0:
#             bit = tempSum % 2 
#             result.append(str(bit))
#             tempSum //= 2 
#         result = ''.join(result[::-1]) #reverse the list 
#         # resultInString = str(result)
#         return result
        
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        result = []

        while i >= 0 or j >= 0 or carry > 0:
            num_a = int(a[i]) if i >= 0 else 0
            num_b = int(b[j]) if j >= 0 else 0

            total_sum = num_a + num_b + carry
            current_bit = total_sum % 2
            carry = total_sum // 2

            result.append(str(current_bit))

            i -= 1
            j -= 1
        
        return ''.join(result[::-1])

     
        