class Solution {
    public int maxArea(int[] heights) {
        int left = 0, right = heights.length - 1;
        int max = Integer.MIN_VALUE;
        int area, limit;
        while (left < right) {
            if (heights[left] <= heights[right]){
                area = (right - left) * heights[left++];
            } else {
                area = (right - left) * heights[right--];
            }
            if (max < area) {
                max = area;
            }     
        }
        return max;
    }
}
