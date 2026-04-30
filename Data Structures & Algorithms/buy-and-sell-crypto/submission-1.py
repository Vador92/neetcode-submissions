class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        first, second = 0, 1
        while second < len(prices):
            if prices[second] > prices[first]:
                if prices[second] - prices[first] > ans:
                    ans = prices[second] - prices[first]
                second+=1
            else:
                first += 1
                second = first + 1

        return ans