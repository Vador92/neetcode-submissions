class Solution:
    def findMin(self, nums: List[int]) -> int:
        ans = float("inf")
        left = 0
        right = len(nums) - 1
        while left <= right:
            m = (left + right) // 2
            if nums[m] < ans:
                ans = nums[m]
            if nums[left] < nums[right]:
                right = m - 1
            elif nums[right] < nums[left]:
                if nums[left] > nums[m]:
                    right = m - 1
                else:
                    left = m + 1
            else:
                return ans
        return ans