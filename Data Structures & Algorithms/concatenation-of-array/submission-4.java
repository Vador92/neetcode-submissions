class Solution {
    public int[] getConcatenation(int[] nums) {
        int n = nums.length;
        int[] ans = new int[2*n];
        for(int i = 0; i < n; i++){
            int curr = nums[i];
            ans[i] = curr;
            ans[i + n] = curr;
        }
        return ans;
    }
}