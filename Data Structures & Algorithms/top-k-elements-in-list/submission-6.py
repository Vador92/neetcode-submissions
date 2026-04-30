class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        # section out the nums by frequency
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        # create buckets for different sizes based on val
        most = max(freq.values()) + 1
        buckets = [None]*most

        # check each key value pair, and assign bucket
        for key, value in freq.items():
            if buckets[value] == None:
                buckets[value] = [key]
            else:
                buckets[value].append(key)

        ans = []
        i = len(buckets) - 1
        while len(ans) < k:
            if buckets[i] != None:
                ans.extend(buckets[i])
            i-=1
        return ans
