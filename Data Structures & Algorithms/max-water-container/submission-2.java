class Solution {
    public int maxArea(int[] heights) {
        int left = 0, right = heights.length - 1, max = 0, stop = 0;
        while(left < right) {
            stop = (heights[left] <= heights[right]) ? heights[left] : heights[right];
            if ((stop * (right - left)) > max) {
                max = stop * (right - left);
            }
            if (heights[left] <= heights[right]) {
                left += 1;
            } else {
                right -= 1;
            }
        }
        return max;
    }
}
