class Solution {
    public int trap(int[] height) {
        int left = 0;
        int right = height.length-1;
        int maxleft = 0;
        int maxright = 0;
        int count = 0;
        while(left < right){
            maxleft = Math.max(maxleft, height[left]);
            maxright = Math.max(maxright, height[right]);
            if(maxleft < maxright){
                count += maxleft-height[left++];
            }
            else{
                count += maxright-height[right--];
            }
        }

        return count;
    }
}