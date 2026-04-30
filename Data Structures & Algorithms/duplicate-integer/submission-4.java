class Solution {
    public boolean hasDuplicate(int[] nums) {
        // Since all elements are int, we can create a hashmap.
        // 1. How to create a hashmap in java
        // 2. How to add existing array into hashmap
        Map<Integer, Integer> checkDup = new HashMap<>();
        for (int num : nums){
            if (checkDup.containsKey(num)) {
                return true;
            } 
            checkDup.put(num, 1);
        }
        return false;
    }
}