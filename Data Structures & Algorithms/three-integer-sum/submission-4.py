class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        # checking all numbers before len - 1 not including len - 1
        for i in range(len(nums) - 1):
            left = i + 1
            right = left + 1
            while left < len(nums) - 1:
                if (nums[i]+nums[left]+nums[right] == 0):
                    if (sorted([nums[i], nums[left], nums[right]]) not in ans):
                        ans.append(sorted([nums[i], nums[left], nums[right]]))
                        print(ans)
                print(left, right)
                if right == len(nums) - 1:
                    left += 1
                    right = left + 1
                else:
                    right += 1
        return ans