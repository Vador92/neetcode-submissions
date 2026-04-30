class Solution {
    public boolean hasDuplicate(int[] nums) {
        // Since all elements are int, we can create a hashmap.
        // 1. How to create a hashmap in java
        // 2. How to add existing array into hashmap
        Set<Integer> checkDup = new HashSet<>();
        for (int num : nums){
            if (checkDup.contains(num)) {
                return true;
            } 
            checkDup.add(num);
        }
        return false;
    }
}