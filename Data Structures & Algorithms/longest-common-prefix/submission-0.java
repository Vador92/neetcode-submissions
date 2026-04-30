class Solution {
    public String longestCommonPrefix(String[] strs) {
        // slow way
        String ans = "";
        String check = strs[0];
        for (String curr : strs) {
            if (check.length() > curr.length()) check = curr;
        }
        boolean state = true;
        String longest = "";
        for (int i = 0; i < check.length(); i++){
            longest = check.substring(0, i + 1);
            for (int j = 0; j < strs.length; j++){
                System.out.println(longest.equals(strs[j].substring(0, i + 1)));
                if (!longest.equals(strs[j].substring(0, i + 1))) {
                    state = false;
                    break;
                }
            }
            if (!state) {
                break;
            }
            ans = longest;
        }
        return ans;
    }
}