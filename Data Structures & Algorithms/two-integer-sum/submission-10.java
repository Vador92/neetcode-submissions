class Solution {
    public int[] twoSum(int[] nums, int target) {
        // currently O(n^2), need O(n)
        HashMap<Integer, Integer> diff = new HashMap<>();
        for (int i = 0; i < nums.length; i++){
            if (diff.containsKey(nums[i])) {
                return new int[]{diff.get(nums[i]), i};
            }
            diff.put(target-nums[i], i);
            System.out.println(diff);
        }
        return new int[] {};
    }
}
