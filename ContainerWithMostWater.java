class Solution {
    public int maxArea(int[] height) {
        int left = 0;
        int right = height.length-1;
        int max = 0;
        while(left < right){
            int maxHeight = 0;
            if(height[left] > height[right]){
                maxHeight = height[right];
            }
            else{
                maxHeight = height[left];
            }
            if(maxHeight * (right-left) > max){
                max = maxHeight * (right-left);
            }
            if(height[left] < height[right]){
                left++;
            }
            else{
                right--;
            }
        }
        return max;
    }
}