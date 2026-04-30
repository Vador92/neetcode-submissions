class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int top = 0, bot = matrix.length - 1;
        int last = matrix[0].length - 1;
        while (top < bot){
            int mid = (top + bot) / 2;
            System.out.println(matrix[mid][last]);
            if (matrix[mid][last] == target){
                return true;
            }
            else if (matrix[mid][last] > target){
                if ((matrix[top][last]) < target){
                    top = mid;
                } else {
                    bot = mid;
                }
            } else {
                if (top == mid){
                    top = mid + 1;
                } else {
                    top = mid;
                }
            }
        }
        int left = 0, right = last;
        while (left <= right) {
            int mid = (left+right) / 2;
            if (matrix[top][mid] == target){
                return true;
            } else if (matrix[top][mid] > target){
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        return false;
    }
}
