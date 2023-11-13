class Solution {
    public int maxProfit(int[] prices) {
       int left = 0;
       int right = 1;
       int max = 0;
       while(right < prices.length){
           if(prices[right] - prices[left] > max){
               max = prices[right] - prices[left];
               right++;
           }
           else if(prices[right] - prices[left] < 0 && left < right-1){
               left++;
           }
           else if(prices[right] - prices[left] < 0){
               left++;
               right++;
           }
           else {
               right++;
           }
       }
       return max;
    }
}