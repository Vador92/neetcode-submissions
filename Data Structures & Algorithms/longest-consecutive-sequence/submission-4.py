class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(nums)
        if len(nums) == 1:
            return 1
        ans = 0
        curr = 1
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] == 1:
                curr += 1
                if curr > ans:
                    ans = curr
            elif nums[i] == nums[i-1]:
                if curr > ans:
                    ans = curr
            else:
                curr = 1
        
        return ans
            