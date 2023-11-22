class Solution {
    public int lengthOfLongestSubstring(String s) {
        char[] sarray = s.toCharArray();
        ArrayList<Character> checkrep = new ArrayList<>();
        int maxCount = 0;
        int count = 0;
        for(int i = 0; i < sarray.length; i++){
            if(!checkrep.contains(sarray[i])){
                count++;
                checkrep.add(sarray[i]);
            }
            else{
                if(count > maxCount){
                    maxCount = count;
                }
                while(checkrep.get(0) != sarray[i]){
                    checkrep.remove(0);
                    count--;
                }
                checkrep.remove(0);
                checkrep.add(sarray[i]);
            }
            if(i == sarray.length-1){
                if(count > maxCount){
                    maxCount = count;
                }
            }
        }
        return maxCount;
    }
}