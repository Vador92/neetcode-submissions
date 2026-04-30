class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        most = 0
        left = 0
        right = left + 1
        while right != len(prices):
            if prices[right] - prices[left] > most:
                most = prices[right] - prices[left]
            if right == len(prices) - 1:
                left += 1
                right = left + 1
            else:
                right += 1
        return most