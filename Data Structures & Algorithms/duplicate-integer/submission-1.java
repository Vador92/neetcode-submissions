class Solution {
    public boolean hasDuplicate(int[] nums) {
        ArrayList<Integer> newList = new ArrayList<Integer>();
        for(int i = 0; i < nums.length; i++){
            if(newList.indexOf(nums[i]) == -1){
                newList.add(nums[i]);
            }
            else{
                return true;
            }
        }
        return false;
    }
}
