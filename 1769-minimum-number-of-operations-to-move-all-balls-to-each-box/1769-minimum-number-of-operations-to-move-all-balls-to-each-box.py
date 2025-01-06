class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        res =[]
        for i in range(len(boxes)):
            curr_moves =0
            for j in range(len(boxes)):
                if boxes[j]== '1':
                    curr_moves += abs(i-j)
            res.append(curr_moves)
        return res 
        