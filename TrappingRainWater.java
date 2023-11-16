class Solution {
    public int trap(int[] height) {
        int[] maxleft = new int[height.length];
        int[] maxright = new int[height.length];
        int max = 0;
        for(int i = 0 ; i < height.length; i++){
            maxleft[i] = max;
            if(height[i] > max){
                max = height[i];
            }
        }

        max = 0;
        for(int i = height.length-1 ; i >= 0 ; i--){
            maxright[i] = max;
            if(height[i] > max){
                max = height[i];
            }
        }

        int count = 0;
        for(int i = 0; i < height.length; i++){
            if(Math.min(maxleft[i], maxright[i]) - height[i] > 0){
                count += Math.min(maxleft[i], maxright[i]) - height[i];
            }
        }

        return count;
    }
}