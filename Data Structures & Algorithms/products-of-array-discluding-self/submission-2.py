class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0] * len(nums)
        postfix = [0] * len(nums)
        prefix[0] = nums[0]
        postfix[-1] = nums[-1]
        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i]
        print(nums)
        for j in range(len(nums)-2, -1, -1):
            print(postfix, nums[j])
            postfix[j] = postfix[j+1] * nums[j]
        
        nums[0] = postfix[1]
        nums[-1] = prefix[-2]
        print(nums)
        for i in range(1, len(nums) - 1):
            nums[i] = prefix[i-1] * postfix[i + 1]
        
        return nums
        