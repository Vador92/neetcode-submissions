class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> checkDup = new HashSet<>();
        for (int num : nums){
            if (checkDup.contains(num)) return true;
            checkDup.add(num);
        }
        return false;
    }
}