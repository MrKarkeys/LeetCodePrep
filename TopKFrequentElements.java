class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer, Integer> count = new HashMap<>();
        ArrayList<Integer> keys = new ArrayList<>();
        int left = 0;
        int right = nums.length-1;
        int[] values = new int[k];
        while(left <= right){
            if(!count.containsKey(nums[left])){
                count.put(nums[left], 1);
                keys.add(nums[left]);
            }
            else{
                count.put(nums[left], count.get(nums[left]) + 1);
            }
            left++;

            if(!count.containsKey(nums[right])){
                count.put(nums[right], 1);
                keys.add(nums[right]);
            }
            else{
                count.put(nums[right], count.get(nums[right]) + 1);
            }
            right--;
        }

        for(int i = 0; i < k; i++){
            int max = -1;
            int rem = 0;
            for(int j = 0; j < keys.size(); j++){
                if(count.get(keys.get(j)) > max){
                    max = count.get(keys.get(j));
                    rem = j;
                }
            }
            values[i] = keys.get(rem);
            keys.remove(rem);
        }
        return values;
    }
}