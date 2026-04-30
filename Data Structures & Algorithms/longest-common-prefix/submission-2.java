class Solution {
    public String longestCommonPrefix(String[] strs) {
        // slow way
        String ans = "";
        String check = strs[0];
        for (String curr : strs) {
            if (check.length() > curr.length()) check = curr;
        }
        String longest = "";
        for (int i = 0; i < check.length(); i++){
            longest = check.substring(0, i + 1);
            for (int j = 0; j < strs.length; j++){
                if (!longest.equals(strs[j].substring(0, i + 1))) {
                    return ans;
                }
            }
            ans = longest;
        }
        return ans;
    }
}