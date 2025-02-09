class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        queue = deque([])
        elapse = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    queue.append([i,j])
        directions = [[-1,0],[1,0],[0,1],[0,-1]]
        while queue:
            q = len(queue)
            newRotten = False
            for i in range(q):
                x,y = queue.popleft()
                
                for dx,dy in directions:
                    new_x = x+dx
                    new_y = y + dy
                    if 0 <= new_x < row and 0 <= new_y < col and grid[new_x][new_y]==1:
                        newRotten = True
                        grid[new_x][new_y] = 2
                        queue.append([new_x, new_y])
            if newRotten:
                elapse += 1
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    return -1
        return elapse    

                

        