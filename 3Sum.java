class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        HashSet<List<Integer>> set = new HashSet<>();
        
        Arrays.sort(nums);
        for(int i = 0; i < nums.length; i++){
            int left = i+1;
            int right  = nums.length-1;
            while(left < right){
            ArrayList<Integer> values = new ArrayList<>();
            if((nums[left] + nums[i] + nums[right]) == 0){
                values.add(nums[i]);
                values.add(nums[left]);
                values.add(nums[right]);
                set.add(values);
                left++;
            }
            if((nums[left] + nums[i] + nums[right]) < 0){
                left++;
            }
            else{
                right--;
            }
        }
    }
    ArrayList<List<Integer>> answer = new ArrayList<>(set);
    return answer;
}
}