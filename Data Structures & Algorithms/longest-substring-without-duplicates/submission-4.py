class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curr = ""
        longest = 0
        for char in s:
            # checking each letter
            if char not in curr:
                curr += char
                if len(curr) > longest:
                    longest = len(curr)
            else:
                # start how ever many more from left to the right depending on the index
                # example, index 0 = a and index 3 = a, then move over by 1, 
                # if index 1 = a and index 3 = a, "baca" move to "ca"
                dist = curr.index(char)
                curr = curr[dist+1:] + char
            print(curr)
        return longest