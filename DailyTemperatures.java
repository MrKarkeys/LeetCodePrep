class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        int templen = temperatures.length;
        Stack<Integer> temps = new Stack<>();
        int[] ans = new int[templen];
        for(int i = 0; i < templen; i++){
            if(i+1 >= templen){
                ans[i] = 0;
                while(!temps.isEmpty()){
                    ans[temps.pop()] = 0;
                }
            }
            else{
                if(temperatures[i] < temperatures[i+1]){
                    while(!temps.isEmpty() && temperatures[temps.peek()] < temperatures[i+1]){
                        int val = temps.pop();
                        ans[val] = i+1 - val;
                    }
                    ans[i] = 1;
                }
                else{
                    temps.push(i);
                }
            }
        }
        return ans;
    }
}