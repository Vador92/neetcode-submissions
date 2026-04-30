class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        ans = 0
        while left < right:
            curr = 0
            if heights[left] >= heights[right]:
                curr = heights[right] * (right - left)
                right -= 1
            else:
                curr = heights[left] * (right - left)
                left += 1
            if curr > ans:
                ans = curr
        return ans
