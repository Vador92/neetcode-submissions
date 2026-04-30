class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        ans = 0
        while left < right:
            curr = 0
            nI = ""
            if heights[left] >= heights[right]:
                curr = heights[right]
                nI = "r"
            else:
                curr = heights[left]
                nI = "l"
            if curr *  (right - left) > ans:
                ans = curr * (right - left)
            if nI == "r":
                right -=1
            else: 
                left += 1
        return ans

            