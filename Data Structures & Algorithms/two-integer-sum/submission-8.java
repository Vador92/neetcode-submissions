class Solution {
    public int[] twoSum(int[] nums, int target) {
        // currently O(n^2), need O(n)
        Map<Integer, Integer> ans = new HashMap<>(); // saving the index, difference is key, index is value
        for(int i = 0; i < nums.length; i++) {
            System.out.println(target-nums[i]);
            if (ans.get(target - nums[i]) != null){
                return new int[]{ans.get(target - nums[i]), i};
            }
            ans.put(nums[i], i);   
            System.out.println(ans);       
        }
        return new int[]{0,1};
    }
}
