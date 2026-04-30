class Solution {
    public int removeElement(int[] nums, int val) {
        Arrays.sort(nums);
        int right = nums.length - 1;
        int left = 0;
        while (left <= right){
            if (nums[right] == val) {
                right -= 1;
                continue;
            } else if (nums[left] == val) {
                int temp = nums[right];
                nums[right] = nums[left];
                nums[left] = temp;
                right -= 1;
            }
            left += 1;
        }
        return right+1;
    }
}