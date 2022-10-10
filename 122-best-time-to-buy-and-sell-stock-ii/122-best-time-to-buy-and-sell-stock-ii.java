class Solution {
    public int maxProfit(int[] prices) {
        //once we find an increase, do we sell immediately? no
        //we keep on going right until we stop increasing values
        int currMin = prices[0];
        int i = 1; 
        int totalProfit = 0;
        while (i < prices.length){
            if (prices[i] > currMin){
                int j = i;
                while (j+1 < prices.length && prices[j+1] > prices[j]){
                    j++;//exits before j is less than i and before it hits end
                }//j has max
                // System.out.println(j);
                totalProfit += prices[j]-currMin;
                i=j;
                i+=1;
                if (i >= prices.length)
                    return totalProfit;
                currMin = prices[i];
            }else{
                currMin = Math.min(prices[i], currMin);
                i++;
            }
            
            
        }
        return totalProfit;
        
        
    }
}