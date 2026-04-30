class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ans = []
        for i in range(len(numbers)):
            difference = target - numbers[i]
            if difference in numbers:
                if numbers.index(difference) > i:
                    ans = [i+1, numbers.index(difference) + 1]
                    break
        return ans