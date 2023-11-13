class Solution {
    public int longestConsecutive(int[] nums) {
        if(nums.length == 0){
            return 0;
        }
        Arrays.sort(nums);
        int max = 0;
        int count = 1;
        for(int i = 1; i < nums.length; i++){
            if(nums[i-1] == (nums[i]-1) || nums[i-1] == (nums[i])){
                if(nums[i-1] != (nums[i])){
                    count++;
                }
            }
            else{
                if(count  > max){
                    max = count;
                }
                count = 1;
            }
        }
        if(count > max){
            max = count;
        }
        return max;
    }
}