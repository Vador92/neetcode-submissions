class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            for key in dic.keys():
                if nums[i] + dic[key] == target:
                    return [key, i]
            dic[i] = nums[i]
        

                