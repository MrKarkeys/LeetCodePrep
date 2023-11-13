class Solution {
    public int findMin(int[] nums) {
        int min = Integer.MAX_VALUE;
        int left = 0;
        int right = nums.length-1;
        while(left <= right){
            if(min > nums[left]){
                min = nums[left];
            }
            if(min > nums[right]){
                min = nums[right];
            }
            left++;
            right--;
        }
        return min;
    }
}