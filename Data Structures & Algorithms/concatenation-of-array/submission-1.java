class Solution {
    public int[] getConcatenation(int[] nums) {
        int[] ans = new int[2 * nums.length];
        int i = 0;
        for (int curr : nums){
            ans[i] = curr;
            ans[i+nums.length] = curr;
            i +=1;
        }
        return ans;
    }
}