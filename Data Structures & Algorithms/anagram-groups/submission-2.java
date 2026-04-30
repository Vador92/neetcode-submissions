class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        // Creating hashmap of of list of strings, for each word, we sort and dump based on key
        Map<String, List<String>> dict = new HashMap<>();
        List<List<String>> ans = new ArrayList<>();
        for (String curr : strs) {
            String newWord = orderedWord(curr);
            if (dict.get(newWord) == null){
                List<String> newList = new ArrayList<>();
                newList.add(curr);
                dict.put(newWord, newList);
            } else {
                List<String> addList = dict.get(newWord);
                addList.add(curr);
                dict.put(newWord, addList);
            }
        }
        for (List<String> currWords: dict.values()){
            ans.add(currWords);
        }
        return ans;
    }

    public String orderedWord(String curr) {
        char tempArray[] = curr.toCharArray();
        Arrays.sort(tempArray);
        return new String(tempArray);
    }
}
