class Solution {
    public boolean hasDuplicate(int[] nums) {
        // create new set
        Set<Integer> mySet = new HashSet<>();
        for (int num: nums){
            if (mySet.contains(num)) return true;
            mySet.add(num);
        }
        return false;
    }
}