// Last updated: 11/2/2025, 8:22:08 PM
class Solution {
    public int[][] construct2DArray(int[] original, int m, int n) {
        int[][] arr = new int[m][n];
        int count = 0;

        if(original.length != m*n){
            return new int[][]{};
        }

        for(int x = 0; x < m; x++){
            for(int y = 0; y<n; y++){
                arr[x][y] = original[count];
                count++;

            }
        }
        return arr;
    }
}