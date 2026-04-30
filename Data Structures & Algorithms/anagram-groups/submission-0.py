class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {} # hash
        fans = []
        for i in range(len(strs)): # go through each sorted word
            value = "".join(sorted(strs[i]))
            if value in ans:
                ans[value].append(strs[i])
            else:
                ans[value] = [strs[i]]
            
        for val in ans.values():
            fans.append(val)
        return fans
                
