class Solution {
    public int[][] updateMatrix(int[][] mat) {
        int row = mat.length;
        int col = mat[0].length;
        int[][] dist = new int[row][col];
        Queue<int[]> queue = new ArrayDeque<>();
        
        // Initialize dist array and queue
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                if (mat[i][j] == 0) {
                    dist[i][j] = 0;
                    queue.offer(new int[]{i, j});
                } else {
                    dist[i][j] = Integer.MAX_VALUE;
                }
            }
        }
        
        // Directions: up, down, left, right
        int[][] directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        
        // BFS
        while (!queue.isEmpty()) {
            int[] curr = queue.poll();
            int r = curr[0];
            int c = curr[1];
            
            for (int[] dir : directions) {
                int newRow = r + dir[0];
                int newCol = c + dir[1];
                
                if (newRow >= 0 && newRow < row && 
                    newCol >= 0 && newCol < col) {
                    if (dist[newRow][newCol] > dist[r][c] + 1) {
                        dist[newRow][newCol] = dist[r][c] + 1;
                        queue.offer(new int[]{newRow, newCol});
                    }
                }
            }
        }
        
        return dist;
    }
}