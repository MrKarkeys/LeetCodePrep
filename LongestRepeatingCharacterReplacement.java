class Solution {
    public int characterReplacement(String s, int k) {
        char[] sarray = s.toCharArray();
        HashMap<Character, Integer> map = new HashMap<>();
        int left = 0;
        int right = 0;
        int totalCount = 0;
        int prev = -1;
        int max = 0;
        while(right < sarray.length){
            if(!map.containsKey(sarray[right])){
                map.put(sarray[right], 1);
            }
            else{
                if(right != prev){
                    int temp = map.get(sarray[right])+1;
                    map.put(sarray[right], temp);
                }
            }
            prev = right;
            max = Math.max(max, map.get(sarray[right]));
            if((right-left+1)-max <= k){
                totalCount = Math.max(totalCount, right-left+1);
                right++;
            }
            else{                  
                int temp = map.get(sarray[left])-1;
                map.put(sarray[left], temp);
                left++;
            }
        }
        return totalCount;
    }
}