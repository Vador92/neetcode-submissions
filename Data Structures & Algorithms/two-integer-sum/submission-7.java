class Solution {
    public int[] twoSum(int[] nums, int target) {
        int left = 0;
        int right = 1;
        while (true){
            if (nums[left] + nums[right] == target) return new int[]{left, right};
            right += 1;
            if (right > nums.length - 1) {
                left += 1;
                right = left + 1;
            }
        }
    }
}
