class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # length we need to return
        ans = 0

        #left = 0
        right = 0
        word = ""
        # while there are more letters to check
        while right < len(s):
            if s[right] not in word:
                word += s[right]
                right +=1
                if len(word) > ans:
                    ans = len(word)
            else:
                word = word[1:]

        return ans 



        