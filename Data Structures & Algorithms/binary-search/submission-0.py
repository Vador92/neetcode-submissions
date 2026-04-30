class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) -1
        while left <= right:
            m = (left + right) // 2
            print(m)
            if nums[m] == target:
                return m
            if nums[m] > target:
                right = m - 1
            if nums[m] < target:
                left = m + 1
            print(left, right)

        return -1