class Solution {
    public int orangesRotting(int[][] grid) {
        int row = grid.length;
        int col = grid[0].length;
        int freshCount = 0;
        Queue<int[]> queue = new LinkedList<>();

        for (int r = 0; r < row; r++){
            for (int c = 0; c < col; c++){
                if (grid[r][c] == 2){
                    queue.offer(new int[]{r,c});
                }else if (grid[r][c] == 1){
                    freshCount++;
                }
            }
        }

        if (freshCount ==0){
            return 0;
        }
        
        int[][] directions = {{-1,0}, {1,0}, {0,1}, {0,-1}};
        int minutes = 0;

        while (!queue.isEmpty() && freshCount > 0){
            int levelSize = queue.size();
            boolean hasNewRotten = false;

            for (int i = 0; i < levelSize; i++){
                int[] current = queue.poll();
                int curr_r = current[0];
                int curr_c = current[1];

                for (int[] dir:directions){
                    int newRow = curr_r + dir[0];
                    int newCol = curr_c + dir[1];

                    if (0 <= newRow && newRow < row &&
                    0 <=newCol && newCol< col &&
                    grid[newRow][newCol] == 1){
                        grid[newRow][newCol] = 2;
                        freshCount--;
                        queue.offer(new int[]{newRow, newCol});
                        hasNewRotten = true;
                    }
                }
            }
            if (hasNewRotten){
                minutes += 1;
            }
        }
        return freshCount == 0 ? minutes : -1;

    }
}