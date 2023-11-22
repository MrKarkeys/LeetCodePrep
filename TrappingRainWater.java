class Solution {
    public int trap(int[] height) {
        int[] leftH = new int[height.length];
        int[] rightH = new int[height.length];

        int maxleft = 0;
        for(int i = 0; i < height.length; i++){
            leftH[i] = maxleft;
            if(height[i] > maxleft){
                maxleft = height[i];
            }
        }

        int maxright = 0;
        for(int i = height.length-1; i >= 0; i--){
            rightH[i] = maxright;
            if(height[i] > maxright){
                maxright = height[i];
            }
        }

        int count = 0;
        for(int i = 0; i < height.length; i++){
            int minHeight = Math.min(leftH[i], rightH[i]);
            int val = minHeight - height[i];
            if(val > 0){
                count += val;
            }
        }

        return count;
    }
}