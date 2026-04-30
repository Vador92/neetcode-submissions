class Solution {
    public boolean isValid(String s) {
        List<Character> stack = new ArrayList<>();
        Map<Character, Character> check = new HashMap<>();
        check.put('}', '{');
        check.put(']', '[');
        check.put(')', '(');
        for(int i = 0; i < s.length(); i++){
            if (check.get(s.charAt(i)) == null) {
                stack.add(s.charAt(i));
            } else {
                if (stack.size() == 0){
                    return false;
                } else if (stack.remove(stack.size() - 1) != check.get(s.charAt(i))){
                    return false;
                }
            }
        }
        if (stack.size() > 0) {
            return false;
        }
        return true;
    }
}
