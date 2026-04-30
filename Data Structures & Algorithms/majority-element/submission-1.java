class Solution {
    public int majorityElement(int[] nums) {
        if (nums.length == 1){
            return nums[0];
        }
        Map<Integer, Integer> check = new HashMap<>();
        int ans = 0;
        for(int num : nums){
            if (check.get(num) == null) {
                check.put(num, 1);
            }
            else {
                check.put(num, check.get(num) + 1);
                if(check.get(num) > (nums.length / 2)) ans = num;
            }
        }    
        System.out.println(check);
        return ans;
    }
}