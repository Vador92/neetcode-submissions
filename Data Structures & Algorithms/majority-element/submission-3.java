class Solution {
    public int majorityElement(int[] nums) {
        if (nums.length == 1) return nums[0];
        Map<Integer, Integer> check = new HashMap<>();
        for(int num : nums){
            check.put(num, check.getOrDefault(num, 0) + 1);
            if(check.get(num) > (nums.length / 2)) return num;
        }    
        return 0;
    }
}