class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        seen = set()
        result = []
        count = 0
        
        for i in range(len(A)):
            # Add current elements to seen set
            curr_a= A[i]
            curr_b=B[i]
            
            # If same element, count it once
            if A[i] == B[i]:
                count += 1
            # If different elements, check if we've seen them before
            else:
                # Check if B[i] exists in previous A elements
                if B[i] in seen:
                    count += 1
                # Check if A[i] exists in previous B elements
                if A[i] in seen:
                    count += 1
            seen.add(curr_a)
            seen.add(curr_b)
            result.append(count)
        
        return result