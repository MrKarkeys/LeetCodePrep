class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int left = 0;
        int right = matrix[0].length-1;
        int matrixlen = 0;
        while(matrixlen < matrix.length){
            if(matrix[matrixlen][left] == target){
                return true;
            }
            if(matrix[matrixlen][right] == target){
                return true;
            }
            left++;
            right--;
            if(left > right){
                matrixlen++;
                left = 0;
                right = matrix[0].length-1;
            }
        }
        return false;
    }
}