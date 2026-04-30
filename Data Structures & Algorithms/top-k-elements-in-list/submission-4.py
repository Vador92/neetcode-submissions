class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        buckets = [[] for _ in range(len(nums))]
        for key, value in freq.items():
            buckets[value-1].append(key)
        ans = []
        while len(ans) != k:
            stash = buckets.pop()
            if len(stash) == 1:
                ans.append(stash[0])
            elif len(stash) > 1:
                ans.extend(stash)
        return ans