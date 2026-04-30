class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        for i in range(len(nums) - 2):
            left = i + 1
            right = left + 1
            while left < len(nums) - 1:
                if nums[i] + nums[left] + nums[right] == 0:
                    s = [nums[i], nums[left], nums[right]]
                    s = sorted(s)
                    if s not in ans:
                        ans.append(s)
                right += 1
                if right == len(nums):
                    left += 1
                    right = left + 1
        
        return ans