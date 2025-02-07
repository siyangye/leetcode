class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        row = len(mat)
        col = len(mat[0])
        dist = [[float('inf')] * col for i in range(row)]
        queue = deque([])
        for i in range(row):
            for j in range(col):
                if mat[i][j] == 0:
                    dist[i][j] = 0
                    queue.append((i,j))
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        while queue:
            r,c = queue.popleft()
            for x,y in directions:
                new_row = x + r
                new_col = y + c
                if 0 <= new_row < row and 0 <=new_col < col and dist[new_row][new_col] == float('inf'):#if dist[new_row][new_col] == float'inf' -> it means this cell还没有被访问过！
                        dist[new_row][new_col] = dist[r][c] + 1
                        queue.append((new_row, new_col))
        return dist
            
        