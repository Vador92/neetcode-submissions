class Solution {
    public boolean isAnagram(String s, String t) {
        // basically can counter each other
        // r -> +1 for hashmap for r in s
        // r -> -1 for hashmap for r in t
        if (s.length() != t.length()) return false;
        if (s.equals(t)) return true;
        HashMap<Character, Integer> dict = new HashMap<>();
        for (int i = 0; i < s.length(); i++ ){
            char sChar = s.charAt(i);
            char tChar = t.charAt(i);
            if ( dict.containsKey(sChar)) {
                dict.put(sChar, dict.get(sChar)+ 1);
            } else {
                dict.put(sChar, 1);
            }
            if ( dict.containsKey(tChar)) {
                dict.put(tChar, dict.get(tChar) - 1);
            } else {
                dict.put(tChar, -1);
            }
        }
        for (int diff : dict.values()){
            if (diff != 0) return false;
        }
        return true;
    }
}
