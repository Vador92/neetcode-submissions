class Solution {
    public boolean hasDuplicate(int[] nums) {
        // Since all elements are int, we can create a hashmap.
        // 1. How to create a hashmap in java
        // 2. How to add existing array into hashmap

        Map<Integer, Integer> ans = new HashMap<>();
        for(int x : nums){
            System.out.print(ans.get(x) == null);
            if (ans.get(x) == null){
                ans.put(x, 1);
            }
            else {
                return true;
            }
        }
        return false;
    }
}