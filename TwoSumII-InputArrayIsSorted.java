class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int[] val = new int[2];
        int left = 0;
        int right = numbers.length-1;
        while(numbers[left] + numbers[right] != target){
            if(numbers[left] + numbers[right] < target){
                left++;
            }
            else{
                right--;
            }
        }
        val[0] = left+1;
        val[1] = right+1;
        return val;
    }
}