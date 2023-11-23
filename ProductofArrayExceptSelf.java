class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int left = 1;
        int right = 1;
        int result[] = new int[n];
        for(int i = 0; i < nums.length; i++){
            result[i] = 1;
        }
        for(int i = 0; i < nums.length; i++){
            result[i] *= left;
            left *= nums[i]; 
        }
        for(int i = nums.length-1; i >= 0; i--){
            result[i] *= right;
            right *= nums[i];
        }
        return result;
    }
}