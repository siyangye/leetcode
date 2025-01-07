class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        res = [0]*len(boxes)

        count_ones =0
        accumulated_moves = 0

        for i in range(len(boxes)):#[0],c=1,acumu=1,[1],c=2,[3]
            res[i]+= accumulated_moves
            # print(accumulated_moves)
            if boxes[i]=='1':
                count_ones +=1
            accumulated_moves += count_ones
            # print(accumulated_moves)
        print(res)
        left_count_ones =0
        left_accumulated_moves = 0
        n=len(boxes)
        for i in range(n-1,-1,-1):
            res[i]+= left_accumulated_moves
            if boxes[i]=='1':
                left_count_ones +=1
            left_accumulated_moves += left_count_ones
                # print(left_accumulated_moves)
        print(res)
        return res 