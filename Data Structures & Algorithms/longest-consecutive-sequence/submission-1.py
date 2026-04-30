class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        ans = set(nums)
        switch = sorted(ans)
        lo = 1
        curr = 1
        for i in range(1, len(switch)):
            if switch[i] == switch[i-1] + 1:
                curr += 1
                if curr > lo:
                    lo = curr
            else:
                curr = 1
        return lo