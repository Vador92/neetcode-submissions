class Solution {
    public int[] twoSum(int[] nums, int target) {
        int left = 0;
        int right = 1;
        while (left < nums.length - 1){
            if (nums[left] + nums[right] == target) break;
            right += 1;
            if (right > nums.length - 1) {
                left += 1;
                right = left + 1;
            }
        }
        return new int[]{left, right};
    }
}
