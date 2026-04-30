class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grams = {}
        for word in strs:
            curr = "".join(sorted(word))
            print(curr)
            if curr in grams:
                grams[curr].append(word)
            else:
                grams[curr] = [word]

        ans = []
        for key, values in grams.items():
            ans.append(values)
        #append to answer

        return ans