class Solution {
    public boolean isAnagram(String s, String t) {
        // if we have a letter in s, we add 1 to the count,
        // otherwise subtract if found in t
        // space complexity, one hash map
        if (s.length() != t.length()) return false;
        Map<Character, Integer> ans = new HashMap<>();
        for(int i = 0; i < s.length(); i++){
            char sCurr = s.charAt(i);
            char tCurr = t.charAt(i);
            if (ans.get(sCurr) == null){
                ans.put(sCurr, 1);
            } else {
                ans.put(sCurr, ans.get(sCurr) + 1);
            }
            if (ans.get(tCurr) == null) {
                ans.put(tCurr, -1);
            } else{
                ans.put(tCurr, ans.get(tCurr) - 1);
            }
        }
        for (int value : ans.values()){
            if (value != 0){
                return false;
            }
        }

        return true;
    }
}
