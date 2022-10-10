class Solution {
    public int maxProfit(int[] prices) {
        if(prices.length==0) return 0;
        int maxProfit = 0;
        int min = prices[0];
        for(int i = 1; i < prices.length; i++){
            maxProfit = Math.max(prices[i]-min, maxProfit);
            if(min> prices[i])
                min = prices[i];
        }
        return maxProfit;
    }
    
}