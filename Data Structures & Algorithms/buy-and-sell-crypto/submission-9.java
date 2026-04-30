class Solution {
    public int maxProfit(int[] prices) {
        int left = 0, right = 1;
        int profit = 0;
        while(right < prices.length) {
            if (prices[right] - prices[left] > profit) {
                profit = prices[right] - prices[left];
            } // leave this
            System.out.println(left);
            System.out.println(right);

            if (prices[left] > prices[right]) {
                left += 1;
            } else {
                right += 1;
            }
        }
        return profit;
    }
}
